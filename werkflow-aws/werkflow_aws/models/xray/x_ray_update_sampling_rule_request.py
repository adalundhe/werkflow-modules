from __future__ import annotations
from pydantic import BaseModel
from .x_ray_sampling_rule_update import XRaySamplingRuleUpdate


class XRayUpdateSamplingRuleRequest(BaseModel):
    SamplingRuleUpdate: XRaySamplingRuleUpdate
