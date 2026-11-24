from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .scheduler_schedule_group_summary import SchedulerScheduleGroupSummary


class SchedulerListScheduleGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ScheduleGroups: list[SchedulerScheduleGroupSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
