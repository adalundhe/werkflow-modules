from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_connection import EventBridgeConnection


class EventBridgeListConnectionsResponse(BaseModel):
    Connections: list[EventBridgeConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
