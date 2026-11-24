from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class XRayProbabilisticRuleValue(BaseModel):
    DesiredSamplingPercentage: StrictFloat | StrictInt | None = None
    ActualSamplingPercentage: StrictFloat | StrictInt | None = None
