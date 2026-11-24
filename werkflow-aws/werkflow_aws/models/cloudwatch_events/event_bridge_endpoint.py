from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .event_bridge_endpoint_event_bus import EventBridgeEndpointEventBus
from .event_bridge_replication_config import EventBridgeReplicationConfig
from .event_bridge_routing_config import EventBridgeRoutingConfig


class EventBridgeEndpoint(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Arn: StrictStr | None = None
    RoutingConfig: EventBridgeRoutingConfig | None = None
    ReplicationConfig: EventBridgeReplicationConfig | None = None
    EventBuses: list[EventBridgeEndpointEventBus] | None = None
    RoleArn: StrictStr | None = None
    EndpointId: StrictStr | None = None
    EndpointUrl: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
