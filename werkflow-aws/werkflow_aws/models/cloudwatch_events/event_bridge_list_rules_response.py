from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_rule import EventBridgeRule


class EventBridgeListRulesResponse(BaseModel):
    Rules: list[EventBridgeRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
