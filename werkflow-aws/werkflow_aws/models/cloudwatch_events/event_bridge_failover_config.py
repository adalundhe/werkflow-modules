from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_primary import EventBridgePrimary
from .event_bridge_secondary import EventBridgeSecondary


class EventBridgeFailoverConfig(BaseModel):
    Primary: EventBridgePrimary | None = None
    Secondary: EventBridgeSecondary | None = None
