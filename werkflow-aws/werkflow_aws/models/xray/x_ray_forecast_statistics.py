from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayForecastStatistics(BaseModel):
    FaultCountHigh: StrictInt | None = None
    FaultCountLow: StrictInt | None = None
