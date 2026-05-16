import torch
import torchaudio
from torch.utils.data import Dataset

class TTSDataset(Dataset):
    def __init__(self, metadata_path, wav_dir):
        self.data = []
        with open(metadata_path, encoding="utf-8") as f:
            for line in f:
                name, text = line.strip().split("|")
                self.data.append((name, text))

        self.wav_dir = wav_dir
        self.mel_transform = torchaudio.transforms.MelSpectrogram(
            sample_rate=22050,
            n_fft=1024,
            hop_length=256,
            n_mels=80
        )

    def text_to_seq(self, text):
        return torch.tensor([ord(c) % 256 for c in text], dtype=torch.long)

    def __getitem__(self, idx):
        name, text = self.data[idx]

        wav, sr = torchaudio.load(f"{self.wav_dir}/{name}.wav")
        wav = wav.mean(dim=0)

        mel = self.mel_transform(wav)

        return self.text_to_seq(text), mel.T  # [T, 80]

    def __len__(self):
        return len(self.data)