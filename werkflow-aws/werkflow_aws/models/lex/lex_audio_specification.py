from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LexAudioSpecification(BaseModel):
    maxLengthMs: StrictInt | None = None
    endTimeoutMs: StrictInt | None = None
