from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_tag import EventBridgeTag


class EventBridgeTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[EventBridgeTag]
