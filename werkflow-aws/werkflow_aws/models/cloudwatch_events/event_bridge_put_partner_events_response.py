from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .event_bridge_put_partner_events_result_entry import EventBridgePutPartnerEventsResultEntry


class EventBridgePutPartnerEventsResponse(BaseModel):
    FailedEntryCount: StrictInt | None = None
    Entries: list[EventBridgePutPartnerEventsResultEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
