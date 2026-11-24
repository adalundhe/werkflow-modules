from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_deployment_ephemeral_storage import ECSDeploymentEphemeralStorage
from .ecs_load_balancer import ECSLoadBalancer
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_scale import ECSScale
from .ecs_service_registry import ECSServiceRegistry
from .ecs_tag import ECSTag


class ECSTaskSet(BaseModel):
    id: StrictStr | None = None
    taskSetArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    startedBy: StrictStr | None = None
    externalId: StrictStr | None = None
    status: StrictStr | None = None
    taskDefinition: StrictStr | None = None
    computedDesiredCount: StrictInt | None = None
    pendingCount: StrictInt | None = None
    runningCount: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    launchType: StrictStr | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    platformVersion: StrictStr | None = None
    platformFamily: StrictStr | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    scale: ECSScale | None = None
    stabilityStatus: StrictStr | None = None
    stabilityStatusAt: datetime.datetime | StrictStr | None = None
    tags: list[ECSTag] | None = None
    fargateEphemeralStorage: ECSDeploymentEphemeralStorage | None = None
