from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SchedulerScheduleGroupSummary(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModificationDate: datetime.datetime | StrictStr | None = None
