from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_sampling_rule_record import XRaySamplingRuleRecord


class XRayCreateSamplingRuleResponse(BaseModel):
    SamplingRuleRecord: XRaySamplingRuleRecord | None = None
    ResponseMetadata: dict[str, Any] | None = None
