from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .x_ray_sampling_rule import XRaySamplingRule


class XRaySamplingRuleRecord(BaseModel):
    SamplingRule: XRaySamplingRule | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ModifiedAt: datetime.datetime | StrictStr | None = None
