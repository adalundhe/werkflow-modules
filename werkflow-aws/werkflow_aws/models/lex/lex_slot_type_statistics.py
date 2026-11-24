from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LexSlotTypeStatistics(BaseModel):
    discoveredSlotTypeCount: StrictInt | None = None
