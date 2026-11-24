from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EventBridgeReplay(BaseModel):
    ReplayName: StrictStr | None = None
    EventSourceArn: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    EventStartTime: datetime.datetime | StrictStr | None = None
    EventEndTime: datetime.datetime | StrictStr | None = None
    EventLastReplayedTime: datetime.datetime | StrictStr | None = None
    ReplayStartTime: datetime.datetime | StrictStr | None = None
    ReplayEndTime: datetime.datetime | StrictStr | None = None
