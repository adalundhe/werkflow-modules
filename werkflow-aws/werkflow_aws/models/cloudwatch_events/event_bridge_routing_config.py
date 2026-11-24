from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_failover_config import EventBridgeFailoverConfig


class EventBridgeRoutingConfig(BaseModel):
    FailoverConfig: EventBridgeFailoverConfig | None = None
