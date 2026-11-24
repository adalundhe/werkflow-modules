from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightCapacityBytesRangeFilter(BaseModel):
    minBytes: StrictInt | None = None
    maxBytes: StrictInt | None = None
