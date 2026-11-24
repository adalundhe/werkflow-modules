from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_target import EventBridgeTarget


class EventBridgePutTargetsRequest(BaseModel):
    Rule: StrictStr
    Targets: list[EventBridgeTarget]
    EventBusName: StrictStr | None = None
