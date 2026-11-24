from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .scheduler_flexible_time_window import SchedulerFlexibleTimeWindow
from .scheduler_target import SchedulerTarget


class SchedulerCreateScheduleRequest(BaseModel):
    Name: StrictStr
    ScheduleExpression: StrictStr
    Target: SchedulerTarget
    FlexibleTimeWindow: SchedulerFlexibleTimeWindow
    GroupName: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
    KmsKeyArn: StrictStr | None = None
    ClientToken: StrictStr | None = None
    ActionAfterCompletion: Literal['NONE', 'DELETE'] | None = None
