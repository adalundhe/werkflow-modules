from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayRequestImpactStatistics(BaseModel):
    FaultCount: StrictInt | None = None
    OkCount: StrictInt | None = None
    TotalCount: StrictInt | None = None
