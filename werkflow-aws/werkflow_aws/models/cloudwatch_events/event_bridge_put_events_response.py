from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .event_bridge_put_events_result_entry import EventBridgePutEventsResultEntry


class EventBridgePutEventsResponse(BaseModel):
    FailedEntryCount: StrictInt | None = None
    Entries: list[EventBridgePutEventsResultEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
