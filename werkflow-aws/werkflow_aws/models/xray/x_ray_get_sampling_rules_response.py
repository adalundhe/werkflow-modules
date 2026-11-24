from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_sampling_rule_record import XRaySamplingRuleRecord


class XRayGetSamplingRulesResponse(BaseModel):
    SamplingRuleRecords: list[XRaySamplingRuleRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
