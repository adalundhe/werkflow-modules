from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_refresh_schedule_frequency import CloudTrailRefreshScheduleFrequency


class CloudTrailRefreshSchedule(BaseModel):
    Frequency: CloudTrailRefreshScheduleFrequency | None = None
    Status: StrictStr | None = None
    TimeOfDay: StrictStr | None = None
