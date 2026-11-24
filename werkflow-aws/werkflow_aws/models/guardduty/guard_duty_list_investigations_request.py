from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_investigation_filter_criteria import GuardDutyInvestigationFilterCriteria
from .guard_duty_investigation_sort_criteria import GuardDutyInvestigationSortCriteria


class GuardDutyListInvestigationsRequest(BaseModel):
    DetectorId: StrictStr
    FilterCriteria: GuardDutyInvestigationFilterCriteria | None = None
    SortCriteria: GuardDutyInvestigationSortCriteria | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
