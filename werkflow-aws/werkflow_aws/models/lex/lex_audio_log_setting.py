from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_audio_log_destination import LexAudioLogDestination


class LexAudioLogSetting(BaseModel):
    enabled: StrictBool | None = None
    destination: LexAudioLogDestination | None = None
    selectiveLoggingEnabled: StrictBool | None = None
