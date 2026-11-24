from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TranscribeRelativeTimeRange(BaseModel):
    StartPercentage: StrictInt | None = None
    EndPercentage: StrictInt | None = None
    First: StrictInt | None = None
    Last: StrictInt | None = None
