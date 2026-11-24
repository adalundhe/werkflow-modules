from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_deployment_ephemeral_storage import ECSDeploymentEphemeralStorage
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_service_connect_configuration import ECSServiceConnectConfiguration
from .ecs_service_connect_service_resource import ECSServiceConnectServiceResource
from .ecs_service_volume_configuration import ECSServiceVolumeConfiguration
from .ecs_vpc_lattice_configuration import ECSVpcLatticeConfiguration


class ECSDeployment(BaseModel):
    id: StrictStr | None = None
    status: StrictStr | None = None
    taskDefinition: StrictStr | None = None
    desiredCount: StrictInt | None = None
    pendingCount: StrictInt | None = None
    runningCount: StrictInt | None = None
    failedTasks: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    launchType: StrictStr | None = None
    platformVersion: StrictStr | None = None
    platformFamily: StrictStr | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    rolloutState: StrictStr | None = None
    rolloutStateReason: StrictStr | None = None
    serviceConnectConfiguration: ECSServiceConnectConfiguration | None = None
    serviceConnectResources: list[ECSServiceConnectServiceResource] | None = None
    volumeConfigurations: list[ECSServiceVolumeConfiguration] | None = None
    fargateEphemeralStorage: ECSDeploymentEphemeralStorage | None = None
    vpcLatticeConfigurations: list[ECSVpcLatticeConfiguration] | None = None
