from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_replay import EventBridgeReplay


class EventBridgeListReplaysResponse(BaseModel):
    Replays: list[EventBridgeReplay] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
