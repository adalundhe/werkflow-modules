from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_coverage_statistics import GuardDutyCoverageStatistics


class GuardDutyGetCoverageStatisticsResponse(BaseModel):
    CoverageStatistics: GuardDutyCoverageStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
