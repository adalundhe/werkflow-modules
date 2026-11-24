from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyGetCustomDetectionRuleOrgConfigurationRequest(BaseModel):
    RuleId: StrictStr
    Mode: Literal['LIVE', 'DRY_RUN']
