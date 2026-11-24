from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .scheduler_target_summary import SchedulerTargetSummary


class SchedulerScheduleSummary(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    GroupName: StrictStr | None = None
    State: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModificationDate: datetime.datetime | StrictStr | None = None
    Target: SchedulerTargetSummary | None = None
