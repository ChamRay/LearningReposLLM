import json
import math
import os
from dataclasses import dataclass
from typing import List, Tuple

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# 填充符，用来标记文本的内容
PAD = "<pad>"
BOS = "<bos>"
EOS = "<eos>"
UNK = "<unk>"

# 分词函数：去除小写，去掉前后空格，按空格切分token
# 例如："Hello World" -> ["hello", "world"]
def tokenize(text: str) -> List[str]:
    return text.lower().strip().split()

# 读取双语数据，返回映射对
def read_parallel_data(path: str) -> List[Tuple[List[str], List[str]]]:
    pairs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            src, tgt = line.split("\t")
            pairs.append((tokenize(src), tokenize(tgt)))
    return pairs

# 构建词表，即TF嵌入层
def build_vocab(pairs: List[Tuple[List[str], List[str]]]):
    vocab = {PAD: 0, BOS: 1, EOS: 2, UNK: 3}
    for src, tgt in pairs:
        for tok in src + tgt:
            if tok not in vocab:
                vocab[tok] = len(vocab)
    return vocab

# 编码句子，标记句子的开头，结尾
def encode(tokens: List[str], vocab: dict) -> List[int]:
    return [vocab[BOS]] + [vocab.get(t, vocab[UNK]) for t in tokens] + [vocab[EOS]]


class TranslationDataset(Dataset):
    def __init__(self, pairs, vocab):
        self.data = [(encode(src, vocab), encode(tgt, vocab)) for src, tgt in pairs]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# 做batch对齐
def collate_fn(batch):
    srcs, tgts = zip(*batch)
    max_src = max(len(x) for x in srcs)
    max_tgt = max(len(x) for x in tgts)

    src_pad = []
    tgt_pad = []

    for src, tgt in zip(srcs, tgts):
        src_pad.append(src + [0] * (max_src - len(src)))
        tgt_pad.append(tgt + [0] * (max_tgt - len(tgt)))

    return (
        torch.tensor(src_pad, dtype=torch.long),
        torch.tensor(tgt_pad, dtype=torch.long),
    )

# 位置编码
class PositionalEncoding(nn.Module):
    def __init__(self, d_model: int, max_len: int = 512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        pe = pe.unsqueeze(0)  # [1, max_len, d_model]
        self.register_buffer("pe", pe)

    def forward(self, x):
        return x + self.pe[:, : x.size(1)]

# 定义模型
class Seq2SeqTransformer(nn.Module):
    def __init__(self, vocab_size: int, d_model=128, nhead=4, num_layers=2, dim_ff=256, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.src_embed = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.tgt_embed = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.pos = PositionalEncoding(d_model)
        # Transformer主体
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=dim_ff,
            dropout=dropout,
            batch_first=True,
        )
        # 输出层
        self.fc = nn.Linear(d_model, vocab_size)

    # mask
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


# 训练参数
@dataclass
class TrainConfig:
    data_path: str = "data/toy_en_fr.txt"
    artifacts_dir: str = "artifacts"
    batch_size: int = 8
    epochs: int = 200
    lr: float = 1e-3
    d_model: int = 128
    nhead: int = 4
    num_layers: int = 2
    dim_ff: int = 256


def train():
    cfg = TrainConfig()
    os.makedirs(cfg.artifacts_dir, exist_ok=True)

    pairs = read_parallel_data(cfg.data_path)
    vocab = build_vocab(pairs)
    dataset = TranslationDataset(pairs, vocab)
    loader = DataLoader(dataset, batch_size=cfg.batch_size, shuffle=True, collate_fn=collate_fn)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = Seq2SeqTransformer(
        vocab_size=len(vocab),
        d_model=cfg.d_model,
        nhead=cfg.nhead,
        num_layers=cfg.num_layers,
        dim_ff=cfg.dim_ff,
    ).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.lr)
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    model.train()
    for epoch in range(cfg.epochs):
        total_loss = 0.0
        for src, tgt in loader:
            src = src.to(device)
            tgt = tgt.to(device)

            tgt_input = tgt[:, :-1]
            tgt_output = tgt[:, 1:]

            logits = model(src, tgt_input)
            loss = criterion(logits.reshape(-1, logits.size(-1)), tgt_output.reshape(-1))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if (epoch + 1) % 20 == 0:
            print(f"epoch={epoch+1} loss={total_loss/len(loader):.4f}")

    torch.save(model.state_dict(), os.path.join(cfg.artifacts_dir, "model.pt"))

    with open(os.path.join(cfg.artifacts_dir, "vocab.json"), "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    with open(os.path.join(cfg.artifacts_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(
            {
                "vocab_size": len(vocab),
                "d_model": cfg.d_model,
                "nhead": cfg.nhead,
                "num_layers": cfg.num_layers,
                "dim_ff": cfg.dim_ff,
            },
            f,
            indent=2,
        )

    print("training done, artifacts saved to artifacts/")


if __name__ == "__main__":
    train()