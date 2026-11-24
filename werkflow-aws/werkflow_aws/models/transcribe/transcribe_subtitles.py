from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class TranscribeSubtitles(BaseModel):
    Formats: list[Literal['vtt', 'srt']] | None = None
    OutputStartIndex: StrictInt | None = None
