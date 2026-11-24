from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_speech_model_config import LexSpeechModelConfig


class LexSpeechRecognitionSettings(BaseModel):
    speechModelPreference: StrictStr | None = None
    speechModelConfig: LexSpeechModelConfig | None = None
