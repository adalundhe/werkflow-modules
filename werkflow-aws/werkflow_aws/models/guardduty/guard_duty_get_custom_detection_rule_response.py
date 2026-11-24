from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_rule_detail import GuardDutyRuleDetail


class GuardDutyGetCustomDetectionRuleResponse(BaseModel):
    Rule: GuardDutyRuleDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
