from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_association_detail import GuardDutyAssociationDetail


class GuardDutyGetCustomDetectionRuleAssociationResponse(BaseModel):
    RuleAssociation: GuardDutyAssociationDetail | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
