from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .redshift_scheduled_action_filter import RedshiftScheduledActionFilter


class RedshiftDescribeScheduledActionsRequest(BaseModel):
    ScheduledActionName: StrictStr | None = None
    TargetActionType: Literal['ResizeCluster', 'PauseCluster', 'ResumeCluster'] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Active: StrictBool | None = None
    Filters: list[RedshiftScheduledActionFilter] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
