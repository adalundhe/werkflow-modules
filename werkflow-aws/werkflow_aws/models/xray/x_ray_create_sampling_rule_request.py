from __future__ import annotations
from pydantic import BaseModel
from .x_ray_sampling_rule import XRaySamplingRule
from .x_ray_tag import XRayTag


class XRayCreateSamplingRuleRequest(BaseModel):
    SamplingRule: XRaySamplingRule
    Tags: list[XRayTag] | None = None
