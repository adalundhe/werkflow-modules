from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .x_ray_sampling_boost import XRaySamplingBoost


class XRaySamplingTargetDocument(BaseModel):
    RuleName: StrictStr | None = None
    FixedRate: StrictFloat | StrictInt | None = None
    ReservoirQuota: StrictInt | None = None
    ReservoirQuotaTTL: datetime.datetime | StrictStr | None = None
    Interval: StrictInt | None = None
    SamplingBoost: XRaySamplingBoost | None = None
