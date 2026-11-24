from __future__ import annotations
from pydantic import BaseModel
from .route53_arc_assertion_rule_update import Route53ARCAssertionRuleUpdate
from .route53_arc_gating_rule_update import Route53ARCGatingRuleUpdate


class Route53ARCUpdateSafetyRuleRequest(BaseModel):
    AssertionRuleUpdate: Route53ARCAssertionRuleUpdate | None = None
    GatingRuleUpdate: Route53ARCGatingRuleUpdate | None = None
