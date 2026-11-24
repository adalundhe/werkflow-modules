from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .guard_duty_coverage_filter_criteria import GuardDutyCoverageFilterCriteria


class GuardDutyGetCoverageStatisticsRequest(BaseModel):
    DetectorId: StrictStr
    StatisticsType: list[Literal['COUNT_BY_RESOURCE_TYPE', 'COUNT_BY_COVERAGE_STATUS']]
    FilterCriteria: GuardDutyCoverageFilterCriteria | None = None
