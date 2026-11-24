from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetCustomDetectionRuleAssociationRequest(BaseModel):
    RuleId: StrictStr
    AssociationId: StrictStr
