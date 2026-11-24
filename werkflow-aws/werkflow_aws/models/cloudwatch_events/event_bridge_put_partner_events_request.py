from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_put_partner_events_request_entry import EventBridgePutPartnerEventsRequestEntry


class EventBridgePutPartnerEventsRequest(BaseModel):
    Entries: list[EventBridgePutPartnerEventsRequestEntry]
