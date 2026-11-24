from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_replay_destination import EventBridgeReplayDestination


class EventBridgeDescribeReplayResponse(BaseModel):
    ReplayName: StrictStr | None = None
    ReplayArn: StrictStr | None = None
    Description: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    EventSourceArn: StrictStr | None = None
    Destination: EventBridgeReplayDestination | None = None
    EventStartTime: datetime.datetime | StrictStr | None = None
    EventEndTime: datetime.datetime | StrictStr | None = None
    EventLastReplayedTime: datetime.datetime | StrictStr | None = None
    ReplayStartTime: datetime.datetime | StrictStr | None = None
    ReplayEndTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
