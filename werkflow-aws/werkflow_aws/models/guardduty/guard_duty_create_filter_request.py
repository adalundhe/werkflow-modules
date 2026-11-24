from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_criteria import GuardDutyFindingCriteria


class GuardDutyCreateFilterRequest(BaseModel):
    DetectorId: StrictStr
    Name: StrictStr
    FindingCriteria: GuardDutyFindingCriteria
    Description: StrictStr | None = None
    Action: Literal['NOOP', 'ARCHIVE'] | None = None
    Rank: StrictInt | None = None
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
