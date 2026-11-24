from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TranscribeAbsoluteTimeRange(BaseModel):
    StartTime: StrictInt | None = None
    EndTime: StrictInt | None = None
    First: StrictInt | None = None
    Last: StrictInt | None = None
