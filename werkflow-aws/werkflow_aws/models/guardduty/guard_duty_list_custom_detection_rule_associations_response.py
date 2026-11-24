from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_association_summary import GuardDutyAssociationSummary


class GuardDutyListCustomDetectionRuleAssociationsResponse(BaseModel):
    RuleAssociations: list[GuardDutyAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
