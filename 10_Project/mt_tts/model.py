import torch
import torch.nn as nn

class SimpleTTS(nn.Module):
    def __init__(self, vocab_size=256, d_model=128):
        super().__init__()

        self.embed = nn.Embedding(vocab_size, d_model)

        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model, 4, batch_first=True),
            num_layers=3
        )

        self.decoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model, 4, batch_first=True),
            num_layers=3
        )

        self.linear = nn.Linear(d_model, 80)

    def forward(self, text, max_len=200):
        x = self.embed(text)

        x = self.encoder(x)

        # repeat expansion（关键：代替 duration）
        x = x.repeat_interleave(5, dim=1)

        x = self.decoder(x)

        mel = self.linear(x)

        return mel