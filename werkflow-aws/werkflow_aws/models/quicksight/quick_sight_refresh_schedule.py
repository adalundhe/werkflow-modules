from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_refresh_frequency import QuickSightRefreshFrequency


class QuickSightRefreshSchedule(BaseModel):
    ScheduleId: StrictStr | None = None
    ScheduleFrequency: QuickSightRefreshFrequency | None = None
    StartAfterDateTime: datetime.datetime | StrictStr | None = None
    RefreshType: StrictStr | None = None
    Arn: StrictStr | None = None
