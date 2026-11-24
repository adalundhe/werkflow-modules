from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .redshift_scheduled_action_type import RedshiftScheduledActionType


class RedshiftCreateScheduledActionRequest(BaseModel):
    ScheduledActionName: StrictStr
    TargetAction: RedshiftScheduledActionType
    Schedule: StrictStr
    IamRole: StrictStr
    ScheduledActionDescription: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Enable: StrictBool | None = None
