from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayFaultStatistics(BaseModel):
    OtherCount: StrictInt | None = None
    TotalCount: StrictInt | None = None
