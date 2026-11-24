from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_target import EventBridgeTarget


class EventBridgeListTargetsByRuleResponse(BaseModel):
    Targets: list[EventBridgeTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
