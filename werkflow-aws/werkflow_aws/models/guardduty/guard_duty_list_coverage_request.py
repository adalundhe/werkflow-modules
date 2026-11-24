from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_coverage_filter_criteria import GuardDutyCoverageFilterCriteria
from .guard_duty_coverage_sort_criteria import GuardDutyCoverageSortCriteria


class GuardDutyListCoverageRequest(BaseModel):
    DetectorId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    FilterCriteria: GuardDutyCoverageFilterCriteria | None = None
    SortCriteria: GuardDutyCoverageSortCriteria | None = None
