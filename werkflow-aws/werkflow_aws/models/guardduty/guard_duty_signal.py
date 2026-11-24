from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .guard_duty_activity import GuardDutyActivity
from .guard_duty_indicator import GuardDutyIndicator


class GuardDutySignal(BaseModel):
    Uid: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    FirstSeenAt: datetime.datetime | StrictStr | None = None
    LastSeenAt: datetime.datetime | StrictStr | None = None
    Severity: StrictFloat | StrictInt | None = None
    Count: StrictInt | None = None
    ResourceUids: list[StrictStr] | None = None
    ActorIds: list[StrictStr] | None = None
    EndpointIds: list[StrictStr] | None = None
    SignalIndicators: list[GuardDutyIndicator] | None = None
    Activities: list[GuardDutyActivity] | None = None
