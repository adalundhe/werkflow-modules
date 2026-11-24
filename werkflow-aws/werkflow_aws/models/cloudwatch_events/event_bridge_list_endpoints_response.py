from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_endpoint import EventBridgeEndpoint


class EventBridgeListEndpointsResponse(BaseModel):
    Endpoints: list[EventBridgeEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
