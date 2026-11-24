from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ComputeOptimizerCurrentPerformanceRiskRatings(BaseModel):
    high: StrictInt | None = None
    medium: StrictInt | None = None
    low: StrictInt | None = None
    veryLow: StrictInt | None = None
