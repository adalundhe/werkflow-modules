from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .x_ray_indexing_rule_value import XRayIndexingRuleValue


class XRayIndexingRule(BaseModel):
    Name: StrictStr | None = None
    ModifiedAt: datetime.datetime | StrictStr | None = None
    Rule: XRayIndexingRuleValue | None = None
