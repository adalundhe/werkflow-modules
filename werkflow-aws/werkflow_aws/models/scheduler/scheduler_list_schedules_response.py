from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .scheduler_schedule_summary import SchedulerScheduleSummary


class SchedulerListSchedulesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Schedules: list[SchedulerScheduleSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
