from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeSubtitlesOutput(BaseModel):
    Formats: list[StrictStr] | None = None
    SubtitleFileUris: list[StrictStr] | None = None
    OutputStartIndex: StrictInt | None = None
