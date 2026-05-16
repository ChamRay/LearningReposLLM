import torch

def collate_fn(batch):
    texts, mels = zip(*batch)

    text_lens = [len(t) for t in texts]
    mel_lens = [m.shape[0] for m in mels]

    max_text = max(text_lens)
    max_mel = max(mel_lens)

    text_pad = torch.zeros(len(texts), max_text, dtype=torch.long)
    mel_pad = torch.zeros(len(mels), max_mel, 80)

    for i in range(len(texts)):
        text_pad[i, :text_lens[i]] = texts[i]
        mel_pad[i, :mel_lens[i]] = mels[i]

    return text_pad, mel_pad