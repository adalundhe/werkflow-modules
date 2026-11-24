from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_placement_constraint import ECSPlacementConstraint
from .ecs_placement_strategy import ECSPlacementStrategy
from .ecs_tag import ECSTag
from .ecs_task_override import ECSTaskOverride
from .ecs_task_volume_configuration import ECSTaskVolumeConfiguration


class ECSRunTaskRequest(BaseModel):
    taskDefinition: StrictStr
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    cluster: StrictStr | None = None
    count: StrictInt | None = None
    enableECSManagedTags: StrictBool | None = None
    enableExecuteCommand: StrictBool | None = None
    group: StrictStr | None = None
    launchType: Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES'] | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    overrides: ECSTaskOverride | None = None
    placementConstraints: list[ECSPlacementConstraint] | None = None
    placementStrategy: list[ECSPlacementStrategy] | None = None
    platformVersion: StrictStr | None = None
    propagateTags: Literal['TASK_DEFINITION', 'SERVICE', 'NONE'] | None = None
    referenceId: StrictStr | None = None
    startedBy: StrictStr | None = None
    tags: list[ECSTag] | None = None
    clientToken: StrictStr | None = None
    volumeConfigurations: list[ECSTaskVolumeConfiguration] | None = None
