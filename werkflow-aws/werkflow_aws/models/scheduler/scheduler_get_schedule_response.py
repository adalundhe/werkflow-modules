from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .scheduler_flexible_time_window import SchedulerFlexibleTimeWindow
from .scheduler_target import SchedulerTarget


class SchedulerGetScheduleResponse(BaseModel):
    Arn: StrictStr | None = None
    GroupName: StrictStr | None = None
    Name: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    State: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModificationDate: datetime.datetime | StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    Target: SchedulerTarget | None = None
    FlexibleTimeWindow: SchedulerFlexibleTimeWindow | None = None
    ActionAfterCompletion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
