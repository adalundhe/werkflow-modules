from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetCustomDetectionRuleRequest(BaseModel):
    RuleId: StrictStr
