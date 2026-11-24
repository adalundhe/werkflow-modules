from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_api_destination import EventBridgeApiDestination


class EventBridgeListApiDestinationsResponse(BaseModel):
    ApiDestinations: list[EventBridgeApiDestination] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
