from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyCreateCustomDetectionRuleAssociationRequest(BaseModel):
    RuleId: StrictStr
    Mode: Literal['LIVE', 'DRY_RUN']
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
