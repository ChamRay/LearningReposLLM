import json
import math
from typing import List

import torch
import torch.nn as nn

PAD = "<pad>"
BOS = "<bos>"
EOS = "<eos>"
UNK = "<unk>"


def tokenize(text: str) -> List[str]:
    return text.lower().strip().split()


class PositionalEncoding(nn.Module):
    def __init__(self, d_model: int, max_len: int = 512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        self.register_buffer("pe", pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, : x.size(1)]


class Seq2SeqTransformer(nn.Module):
    def __init__(self, vocab_size: int, d_model=128, nhead=4, num_layers=2, dim_ff=256, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.src_embed = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.tgt_embed = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.pos = PositionalEncoding(d_model)
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=dim_ff,
            dropout=dropout,
            batch_first=True,
        )
        self.fc = nn.Linear(d_model, vocab_size)

    def generate_square_subsequent_mask(self, sz: int, device):
        return torch.triu(torch.ones(sz, sz, device=device), diagonal=1).bool()

    def forward(self, src, tgt_input):
        src_key_padding_mask = src.eq(0)
        tgt_key_padding_mask = tgt_input.eq(0)
        tgt_mask = self.generate_square_subsequent_mask(tgt_input.size(1), src.device)

        src_emb = self.pos(self.src_embed(src) * math.sqrt(self.d_model))
        tgt_emb = self.pos(self.tgt_embed(tgt_input) * math.sqrt(self.d_model))

        out = self.transformer(
            src_emb,
            tgt_emb,
            tgt_mask=tgt_mask,
            src_key_padding_mask=src_key_padding_mask,
            tgt_key_padding_mask=tgt_key_padding_mask,
            memory_key_padding_mask=src_key_padding_mask,
        )
        return self.fc(out)

# 推理时，要构建模型
class Translator:
    def __init__(self, artifacts_dir="artifacts", device=None):
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))

        with open(f"{artifacts_dir}/vocab.json", "r", encoding="utf-8") as f:
            self.vocab = json.load(f)
        with open(f"{artifacts_dir}/config.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)

        self.id2tok = {v: k for k, v in self.vocab.items()}
        # 重建模型结构
        self.model = Seq2SeqTransformer(
            vocab_size=cfg["vocab_size"],
            d_model=cfg["d_model"],
            nhead=cfg["nhead"],
            num_layers=cfg["num_layers"],
            dim_ff=cfg["dim_ff"],
        ).to(self.device)
        # 从参数中加载模型并加载权重
        self.model.load_state_dict(torch.load(f"{artifacts_dir}/model.pt", map_location=self.device))
        self.model.eval()
    # 把用户输入的句子编码成模型可理解的张量
    def encode(self, text: str):
        ids = [self.vocab[BOS]]
        ids += [self.vocab.get(t, self.vocab[UNK]) for t in tokenize(text)]
        ids += [self.vocab[EOS]]
        return torch.tensor([ids], dtype=torch.long, device=self.device)
    # 把模型生成的ids还原成文本
    def decode_ids(self, ids):
        toks = []
        for i in ids:
            tok = self.id2tok.get(int(i), UNK)
            if tok in (BOS, EOS, PAD):
                continue
            toks.append(tok)
        return " ".join(toks)

    @torch.no_grad()
    def translate(self, text: str, max_len: int = 20):
        src = self.encode(text)
        tgt = torch.tensor([[self.vocab[BOS]]], dtype=torch.long, device=self.device)

        for _ in range(max_len):
            logits = self.model(src, tgt)
            next_id = logits[:, -1, :].argmax(dim=-1, keepdim=True)
            tgt = torch.cat([tgt, next_id], dim=1)
            if next_id.item() == self.vocab[EOS]:
                break

        return self.decode_ids(tgt[0].tolist())


if __name__ == "__main__":
    t = Translator()
    print(t.translate("hello"))
    print(t.translate("do you speak"))