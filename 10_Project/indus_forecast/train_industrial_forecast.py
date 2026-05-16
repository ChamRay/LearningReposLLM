import os
import joblib
import numpy as np
import pandas as pd
from dataclasses import dataclass

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler


@dataclass
class Config:
    csv_path: str = "data/industrial_timeseries.csv"
    target_col: str = "temperature"
    feature_cols: tuple = ("temperature", "pressure", "vibration", "current", "flow", "target_load")
    seq_len: int = 60
    pred_len: int = 10
    batch_size: int = 64
    hidden_size: int = 128
    num_layers: int = 2
    dropout: float = 0.2
    lr: float = 1e-3
    epochs: int = 20
    train_ratio: float = 0.8
    model_dir: str = "industrial_artifacts"


class TimeSeriesDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


class LSTMForecaster(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, pred_len, dropout=0.2):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, pred_len),
        )

    def forward(self, x):
        # x: [B, T, F]
        out, _ = self.lstm(x)
        last_hidden = out[:, -1, :]   # 取最后一个时间步
        pred = self.head(last_hidden) # [B, pred_len]
        return pred


def load_and_clean_data(cfg: Config):
    df = pd.read_csv(cfg.csv_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    # 只保留需要的列
    cols = ["timestamp"] + list(cfg.feature_cols)
    df = df[cols]

    # 缺失值处理：前向填充 + 后向填充
    df = df.ffill().bfill()

    # 简单异常值裁剪（示例）
    for col in cfg.feature_cols:
        q1 = df[col].quantile(0.01)
        q99 = df[col].quantile(0.99)
        df[col] = df[col].clip(q1, q99)

    return df


def build_windows(data_array, target_index, seq_len, pred_len):
    X, y = [], []
    total_len = len(data_array)

    for i in range(total_len - seq_len - pred_len + 1):
        X.append(data_array[i:i + seq_len])
        y.append(data_array[i + seq_len:i + seq_len + pred_len, target_index])

    return np.array(X), np.array(y)


def train():
    cfg = Config()
    os.makedirs(cfg.model_dir, exist_ok=True)

    df = load_and_clean_data(cfg)

    feature_data = df[list(cfg.feature_cols)].values
    target_index = list(cfg.feature_cols).index(cfg.target_col)

    # 训练集 / 测试集切分
    split_idx = int(len(feature_data) * cfg.train_ratio)
    train_raw = feature_data[:split_idx]
    test_raw = feature_data[split_idx - cfg.seq_len - cfg.pred_len + 1:]

    scaler = StandardScaler()
    train_scaled = scaler.fit_transform(train_raw)
    test_scaled = scaler.transform(test_raw)

    X_train, y_train = build_windows(train_scaled, target_index, cfg.seq_len, cfg.pred_len)
    X_test, y_test = build_windows(test_scaled, target_index, cfg.seq_len, cfg.pred_len)

    train_ds = TimeSeriesDataset(X_train, y_train)
    test_ds = TimeSeriesDataset(X_test, y_test)

    train_loader = DataLoader(train_ds, batch_size=cfg.batch_size, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=cfg.batch_size, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = LSTMForecaster(
        input_size=len(cfg.feature_cols),
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        pred_len=cfg.pred_len,
        dropout=cfg.dropout,
    ).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.lr)
    criterion = nn.MSELoss()

    best_val = float("inf")

    for epoch in range(cfg.epochs):
        model.train()
        train_loss = 0.0

        for X_batch, y_batch in train_loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            pred = model(X_batch)
            loss = criterion(pred, y_batch)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for X_batch, y_batch in test_loader:
                X_batch = X_batch.to(device)
                y_batch = y_batch.to(device)
                pred = model(X_batch)
                loss = criterion(pred, y_batch)
                val_loss += loss.item()

        train_loss /= len(train_loader)
        val_loss /= len(test_loader)

        print(f"epoch={epoch+1} train_loss={train_loss:.6f} val_loss={val_loss:.6f}")

        if val_loss < best_val:
            best_val = val_loss
            torch.save(model.state_dict(), os.path.join(cfg.model_dir, "model.pt"))

    joblib.dump(scaler, os.path.join(cfg.model_dir, "scaler.pkl"))
    joblib.dump(cfg, os.path.join(cfg.model_dir, "config.pkl"))

    print("training done. artifacts saved in", cfg.model_dir)


if __name__ == "__main__":
    train()