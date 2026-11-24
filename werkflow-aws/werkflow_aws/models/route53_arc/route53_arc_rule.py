from __future__ import annotations
from pydantic import BaseModel
from .route53_arc_assertion_rule import Route53ARCAssertionRule
from .route53_arc_gating_rule import Route53ARCGatingRule


class Route53ARCRule(BaseModel):
    ASSERTION: Route53ARCAssertionRule | None = None
    GATING: Route53ARCGatingRule | None = None
