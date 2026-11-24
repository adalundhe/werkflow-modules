from __future__ import annotations
from pydantic import BaseModel
from .x_ray_probabilistic_rule_value import XRayProbabilisticRuleValue


class XRayIndexingRuleValue(BaseModel):
    Probabilistic: XRayProbabilisticRuleValue | None = None
