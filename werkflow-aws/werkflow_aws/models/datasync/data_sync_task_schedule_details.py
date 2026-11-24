from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataSyncTaskScheduleDetails(BaseModel):
    StatusUpdateTime: datetime.datetime | StrictStr | None = None
    DisabledReason: StrictStr | None = None
    DisabledBy: StrictStr | None = None
