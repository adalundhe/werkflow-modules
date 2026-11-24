from __future__ import annotations
from pydantic import BaseModel
from .lex_audio_log_setting import LexAudioLogSetting
from .lex_text_log_setting import LexTextLogSetting


class LexConversationLogSettings(BaseModel):
    textLogSettings: list[LexTextLogSetting] | None = None
    audioLogSettings: list[LexAudioLogSetting] | None = None
