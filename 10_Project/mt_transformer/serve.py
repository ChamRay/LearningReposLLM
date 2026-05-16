from fastapi import FastAPI
from pydantic import BaseModel

from export import Translator

app = FastAPI(title="Transformer MT Demo")
translator = Translator()


class TranslateRequest(BaseModel):
    text: str


class TranslateResponse(BaseModel):
    translation: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest):
    result = translator.translate(req.text)
    return TranslateResponse(translation=result)