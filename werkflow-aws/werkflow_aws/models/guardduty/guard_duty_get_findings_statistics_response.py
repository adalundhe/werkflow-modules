from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_finding_statistics import GuardDutyFindingStatistics


class GuardDutyGetFindingsStatisticsResponse(BaseModel):
    FindingStatistics: GuardDutyFindingStatistics | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
