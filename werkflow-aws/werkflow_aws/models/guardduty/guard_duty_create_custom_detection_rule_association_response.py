from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_association_detail import GuardDutyAssociationDetail


class GuardDutyCreateCustomDetectionRuleAssociationResponse(BaseModel):
    RuleAssociation: GuardDutyAssociationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
