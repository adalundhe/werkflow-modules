from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyUpdateCustomDetectionRuleAssociationRequest(BaseModel):
    RuleId: StrictStr
    AssociationId: StrictStr
    Mode: Literal['LIVE', 'DRY_RUN']
