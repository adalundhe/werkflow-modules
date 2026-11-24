from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSNvidiaMpsAllocation(BaseModel):
    memory: StrictInt | None = None
    maxComputePercent: StrictInt | None = None
