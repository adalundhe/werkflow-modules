from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .lightsail_time_period import LightsailTimePeriod


class LightsailEstimateByTime(BaseModel):
    usageCost: StrictFloat | StrictInt | None = None
    pricingUnit: StrictStr | None = None
    unit: StrictFloat | StrictInt | None = None
    currency: StrictStr | None = None
    timePeriod: LightsailTimePeriod | None = None
