from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_indexing_rule_value_update import XRayIndexingRuleValueUpdate


class XRayUpdateIndexingRuleRequest(BaseModel):
    Name: StrictStr
    Rule: XRayIndexingRuleValueUpdate
