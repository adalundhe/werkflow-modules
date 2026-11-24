from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_endpoint_event_bus import EventBridgeEndpointEventBus
from .event_bridge_replication_config import EventBridgeReplicationConfig
from .event_bridge_routing_config import EventBridgeRoutingConfig


class EventBridgeCreateEndpointRequest(BaseModel):
    Name: StrictStr
    RoutingConfig: EventBridgeRoutingConfig
    EventBuses: list[EventBridgeEndpointEventBus]
    Description: StrictStr | None = None
    ReplicationConfig: EventBridgeReplicationConfig | None = None
    RoleArn: StrictStr | None = None
