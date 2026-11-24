from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyCreateCustomDetectionRuleOrgConfigurationRequest(BaseModel):
    RuleId: StrictStr
    Mode: Literal['LIVE', 'DRY_RUN']
    IncludeAccountIds: list[StrictStr] | None = None
    ExcludeAccountIds: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
