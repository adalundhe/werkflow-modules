from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_estimate_by_time import LightsailEstimateByTime


class LightsailCostEstimate(BaseModel):
    usageType: StrictStr | None = None
    resultsByTime: list[LightsailEstimateByTime] | None = None
