from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_arc_new_assertion_rule import Route53ARCNewAssertionRule
from .route53_arc_new_gating_rule import Route53ARCNewGatingRule


class Route53ARCCreateSafetyRuleRequest(BaseModel):
    AssertionRule: Route53ARCNewAssertionRule | None = None
    ClientToken: StrictStr | None = None
    GatingRule: Route53ARCNewGatingRule | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
