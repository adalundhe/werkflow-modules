from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_put_events_request_entry import EventBridgePutEventsRequestEntry


class EventBridgePutEventsRequest(BaseModel):
    Entries: list[EventBridgePutEventsRequestEntry]
    EndpointId: StrictStr | None = None
