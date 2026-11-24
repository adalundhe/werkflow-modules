from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayErrorStatistics(BaseModel):
    ThrottleCount: StrictInt | None = None
    OtherCount: StrictInt | None = None
    TotalCount: StrictInt | None = None
