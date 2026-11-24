from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .event_bridge_replay_destination import EventBridgeReplayDestination


class EventBridgeStartReplayRequest(BaseModel):
    ReplayName: StrictStr
    EventSourceArn: StrictStr
    EventStartTime: datetime.datetime | StrictStr
    EventEndTime: datetime.datetime | StrictStr
    Destination: EventBridgeReplayDestination
    Description: StrictStr | None = None
