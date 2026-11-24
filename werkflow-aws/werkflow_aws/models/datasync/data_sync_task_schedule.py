from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncTaskSchedule(BaseModel):
    ScheduleExpression: StrictStr | None = None
    Status: StrictStr | None = None
