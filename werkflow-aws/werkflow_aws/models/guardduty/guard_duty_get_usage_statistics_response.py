from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_usage_statistics import GuardDutyUsageStatistics


class GuardDutyGetUsageStatisticsResponse(BaseModel):
    UsageStatistics: GuardDutyUsageStatistics | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
