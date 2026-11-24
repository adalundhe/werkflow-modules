from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_sort_criteria import GuardDutySortCriteria


class GuardDutyGetFindingsRequest(BaseModel):
    DetectorId: StrictStr
    FindingIds: list[StrictStr]
    SortCriteria: GuardDutySortCriteria | None = None
