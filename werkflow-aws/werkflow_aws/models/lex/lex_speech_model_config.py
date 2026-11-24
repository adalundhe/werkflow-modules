from __future__ import annotations
from pydantic import BaseModel
from .lex_deepgram_speech_model_config import LexDeepgramSpeechModelConfig


class LexSpeechModelConfig(BaseModel):
    deepgramConfig: LexDeepgramSpeechModelConfig | None = None
