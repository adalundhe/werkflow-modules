from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class XRayProbabilisticRuleValueUpdate(BaseModel):
    DesiredSamplingPercentage: StrictFloat | StrictInt
