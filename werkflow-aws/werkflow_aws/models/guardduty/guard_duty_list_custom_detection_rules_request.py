from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_detection_rule_filter import GuardDutyDetectionRuleFilter


class GuardDutyListCustomDetectionRulesRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[GuardDutyDetectionRuleFilter] | None = None
