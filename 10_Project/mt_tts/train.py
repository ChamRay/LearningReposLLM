import torch
from torch.utils.data import DataLoader
from dataset import TTSDataset
from model import SimpleTTS
from utils import collate_fn

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = TTSDataset("data/metadata.csv", "data/wavs")
loader = DataLoader(dataset, batch_size=8, shuffle=True, collate_fn=collate_fn)

model = SimpleTTS().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = torch.nn.L1Loss()

for epoch in range(20):
    total_loss = 0

    for text, mel in loader:
        text, mel = text.to(device), mel.to(device)

        pred = model(text)

        min_len = min(pred.shape[1], mel.shape[1])
        pred = pred[:, :min_len, :]
        mel = mel[:, :min_len, :]

        loss = criterion(pred, mel)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch} Loss {total_loss:.4f}")

torch.save(model.state_dict(), "tts.pth")