from __future__ import annotations
from pydantic import BaseModel
from .lex_speech_foundation_model import LexSpeechFoundationModel


class LexUnifiedSpeechSettings(BaseModel):
    speechFoundationModel: LexSpeechFoundationModel | None = None
