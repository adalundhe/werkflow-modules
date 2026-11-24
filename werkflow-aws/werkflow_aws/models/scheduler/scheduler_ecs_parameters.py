from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .scheduler_capacity_provider_strategy_item import SchedulerCapacityProviderStrategyItem
from .scheduler_network_configuration import SchedulerNetworkConfiguration
from .scheduler_placement_constraint import SchedulerPlacementConstraint
from .scheduler_placement_strategy import SchedulerPlacementStrategy


class SchedulerEcsParameters(BaseModel):
    TaskDefinitionArn: StrictStr | None = None
    TaskCount: StrictInt | None = None
    LaunchType: StrictStr | None = None
    NetworkConfiguration: SchedulerNetworkConfiguration | None = None
    PlatformVersion: StrictStr | None = None
    Group: StrictStr | None = None
    CapacityProviderStrategy: list[SchedulerCapacityProviderStrategyItem] | None = None
    EnableECSManagedTags: StrictBool | None = None
    EnableExecuteCommand: StrictBool | None = None
    PlacementConstraints: list[SchedulerPlacementConstraint] | None = None
    PlacementStrategy: list[SchedulerPlacementStrategy] | None = None
    PropagateTags: StrictStr | None = None
    ReferenceId: StrictStr | None = None
    Tags: list[dict[StrictStr, StrictStr]] | None = None
