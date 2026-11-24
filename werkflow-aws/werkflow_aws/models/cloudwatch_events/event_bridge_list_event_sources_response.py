from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_event_source import EventBridgeEventSource


class EventBridgeListEventSourcesResponse(BaseModel):
    EventSources: list[EventBridgeEventSource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
