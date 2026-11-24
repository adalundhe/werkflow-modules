from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .event_bridge_capacity_provider_strategy_item import EventBridgeCapacityProviderStrategyItem
from .event_bridge_network_configuration import EventBridgeNetworkConfiguration
from .event_bridge_placement_constraint import EventBridgePlacementConstraint
from .event_bridge_placement_strategy import EventBridgePlacementStrategy
from .event_bridge_tag import EventBridgeTag


class EventBridgeEcsParameters(BaseModel):
    TaskDefinitionArn: StrictStr | None = None
    TaskCount: StrictInt | None = None
    LaunchType: StrictStr | None = None
    NetworkConfiguration: EventBridgeNetworkConfiguration | None = None
    PlatformVersion: StrictStr | None = None
    Group: StrictStr | None = None
    CapacityProviderStrategy: list[EventBridgeCapacityProviderStrategyItem] | None = None
    EnableECSManagedTags: StrictBool | None = None
    EnableExecuteCommand: StrictBool | None = None
    PlacementConstraints: list[EventBridgePlacementConstraint] | None = None
    PlacementStrategy: list[EventBridgePlacementStrategy] | None = None
    PropagateTags: StrictStr | None = None
    ReferenceId: StrictStr | None = None
    Tags: list[EventBridgeTag] | None = None
