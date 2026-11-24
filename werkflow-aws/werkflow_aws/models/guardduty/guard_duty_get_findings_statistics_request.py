from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_criteria import GuardDutyFindingCriteria


class GuardDutyGetFindingsStatisticsRequest(BaseModel):
    DetectorId: StrictStr
    FindingStatisticTypes: list[Literal['COUNT_BY_SEVERITY']] | None = None
    FindingCriteria: GuardDutyFindingCriteria | None = None
    GroupBy: Literal['ACCOUNT', 'DATE', 'FINDING_TYPE', 'RESOURCE', 'SEVERITY'] | None = None
    OrderBy: Literal['ASC', 'DESC'] | None = None
    MaxResults: StrictInt | None = None
