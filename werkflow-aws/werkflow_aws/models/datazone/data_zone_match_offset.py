from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataZoneMatchOffset(BaseModel):
    startOffset: StrictInt | None = None
    endOffset: StrictInt | None = None
