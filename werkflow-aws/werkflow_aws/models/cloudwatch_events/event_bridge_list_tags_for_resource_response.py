from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .event_bridge_tag import EventBridgeTag


class EventBridgeListTagsForResourceResponse(BaseModel):
    Tags: list[EventBridgeTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
