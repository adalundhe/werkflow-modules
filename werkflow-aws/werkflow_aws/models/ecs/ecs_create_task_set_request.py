from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_load_balancer import ECSLoadBalancer
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_scale import ECSScale
from .ecs_service_registry import ECSServiceRegistry
from .ecs_tag import ECSTag


class ECSCreateTaskSetRequest(BaseModel):
    service: StrictStr
    cluster: StrictStr
    taskDefinition: StrictStr
    externalId: StrictStr | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    launchType: Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES'] | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    platformVersion: StrictStr | None = None
    scale: ECSScale | None = None
    clientToken: StrictStr | None = None
    tags: list[ECSTag] | None = None
