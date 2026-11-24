from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LexIntentStatistics(BaseModel):
    discoveredIntentCount: StrictInt | None = None
