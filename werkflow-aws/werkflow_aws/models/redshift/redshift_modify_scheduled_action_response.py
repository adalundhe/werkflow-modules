from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_scheduled_action_type import RedshiftScheduledActionType


class RedshiftModifyScheduledActionResponse(BaseModel):
    ScheduledActionName: StrictStr | None = None
    TargetAction: RedshiftScheduledActionType | None = None
    Schedule: StrictStr | None = None
    IamRole: StrictStr | None = None
    ScheduledActionDescription: StrictStr | None = None
    State: StrictStr | None = None
    NextInvocations: list[datetime.datetime | StrictStr] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
