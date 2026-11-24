from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_criteria import GuardDutyFindingCriteria


class GuardDutyUpdateFilterRequest(BaseModel):
    DetectorId: StrictStr
    FilterName: StrictStr
    Description: StrictStr | None = None
    Action: Literal['NOOP', 'ARCHIVE'] | None = None
    Rank: StrictInt | None = None
    FindingCriteria: GuardDutyFindingCriteria | None = None
