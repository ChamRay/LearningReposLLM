import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn


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
        out, _ = self.lstm(x)
        last_hidden = out[:, -1, :]
        pred = self.head(last_hidden)
        return pred


def load_model(model_dir="industrial_artifacts"):
    cfg = joblib.load(f"{model_dir}/config.pkl")
    scaler = joblib.load(f"{model_dir}/scaler.pkl")

    model = LSTMForecaster(
        input_size=len(cfg.feature_cols),
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        pred_len=cfg.pred_len,
        dropout=cfg.dropout,
    )

    model.load_state_dict(torch.load(f"{model_dir}/model.pt", map_location="cpu"))
    model.eval()
    return model, scaler, cfg


def predict_next_steps(recent_df: pd.DataFrame, model_dir="industrial_artifacts"):
    model, scaler, cfg = load_model(model_dir)

    feature_df = recent_df[list(cfg.feature_cols)].copy()
    x = scaler.transform(feature_df.values)
    x = torch.tensor(x[np.newaxis, :, :], dtype=torch.float32)

    with torch.no_grad():
        pred_scaled = model(x).numpy()[0]

    # 反归一化目标列
    target_idx = list(cfg.feature_cols).index(cfg.target_col)
    mean = scaler.mean_[target_idx]
    std = scaler.scale_[target_idx]
    pred = pred_scaled * std + mean

    return pred


if __name__ == "__main__":
    df = pd.read_csv("industrial_timeseries.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    recent = df.tail(60)
    pred = predict_next_steps(recent)
    print("future prediction:", pred)