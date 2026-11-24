from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteCustomDetectionRuleAssociationRequest(BaseModel):
    RuleId: StrictStr
    AssociationId: StrictStr
