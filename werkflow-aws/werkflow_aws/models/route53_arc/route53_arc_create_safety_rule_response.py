from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_arc_assertion_rule import Route53ARCAssertionRule
from .route53_arc_gating_rule import Route53ARCGatingRule


class Route53ARCCreateSafetyRuleResponse(BaseModel):
    AssertionRule: Route53ARCAssertionRule | None = None
    GatingRule: Route53ARCGatingRule | None = None
    ResponseMetadata: dict[str, Any] | None = None
