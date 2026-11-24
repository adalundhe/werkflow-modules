from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_endpoint_event_bus import EventBridgeEndpointEventBus
from .event_bridge_replication_config import EventBridgeReplicationConfig
from .event_bridge_routing_config import EventBridgeRoutingConfig


class EventBridgeCreateEndpointResponse(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    RoutingConfig: EventBridgeRoutingConfig | None = None
    ReplicationConfig: EventBridgeReplicationConfig | None = None
    EventBuses: list[EventBridgeEndpointEventBus] | None = None
    RoleArn: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
