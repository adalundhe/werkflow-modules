from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_text_log_destination import LexTextLogDestination


class LexTextLogSetting(BaseModel):
    enabled: StrictBool | None = None
    destination: LexTextLogDestination | None = None
    selectiveLoggingEnabled: StrictBool | None = None
