from __future__ import annotations
from pydantic import BaseModel
from .x_ray_probabilistic_rule_value_update import XRayProbabilisticRuleValueUpdate


class XRayIndexingRuleValueUpdate(BaseModel):
    Probabilistic: XRayProbabilisticRuleValueUpdate | None = None
