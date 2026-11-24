from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_rule_summary import GuardDutyRuleSummary


class GuardDutyListCustomDetectionRulesResponse(BaseModel):
    Rules: list[GuardDutyRuleSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
