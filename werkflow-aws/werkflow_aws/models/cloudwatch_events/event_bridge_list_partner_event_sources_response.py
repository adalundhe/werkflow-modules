from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_partner_event_source import EventBridgePartnerEventSource


class EventBridgeListPartnerEventSourcesResponse(BaseModel):
    PartnerEventSources: list[EventBridgePartnerEventSource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
