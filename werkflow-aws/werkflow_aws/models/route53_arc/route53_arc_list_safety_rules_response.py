from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_arc_rule import Route53ARCRule


class Route53ARCListSafetyRulesResponse(BaseModel):
    NextToken: StrictStr | None = None
    SafetyRules: list[Route53ARCRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
