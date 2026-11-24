from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_criteria import GuardDutyFindingCriteria
from .guard_duty_sort_criteria import GuardDutySortCriteria


class GuardDutyListFindingsRequest(BaseModel):
    DetectorId: StrictStr
    FindingCriteria: GuardDutyFindingCriteria | None = None
    SortCriteria: GuardDutySortCriteria | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
