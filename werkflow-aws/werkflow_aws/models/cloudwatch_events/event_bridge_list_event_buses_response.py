from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_event_bus import EventBridgeEventBus


class EventBridgeListEventBusesResponse(BaseModel):
    EventBuses: list[EventBridgeEventBus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
