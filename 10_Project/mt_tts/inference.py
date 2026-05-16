import torch
import torchaudio
from model import SimpleTTS

model = SimpleTTS()
model.load_state_dict(torch.load("tts.pth"))
model.eval()

text = torch.tensor([[ord(c) % 256 for c in "hello"]])

with torch.no_grad():
    mel = model(text)

mel = mel[0].transpose(0,1)

griffin = torchaudio.transforms.GriffinLim(n_fft=1024)
spec = torchaudio.transforms.InverseMelScale(n_stft=1024)(mel)
wav = griffin(spec)

torchaudio.save("out.wav", wav.unsqueeze(0), 22050)