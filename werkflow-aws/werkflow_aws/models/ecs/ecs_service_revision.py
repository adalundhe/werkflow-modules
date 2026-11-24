from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_container_image import ECSContainerImage
from .ecs_deployment_ephemeral_storage import ECSDeploymentEphemeralStorage
from .ecs_gateway_connector import ECSGatewayConnector
from .ecs_load_balancer import ECSLoadBalancer
from .ecs_managed_resources import ECSManagedResources
from .ecs_monitoring_configuration import ECSMonitoringConfiguration
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_resolved_configuration import ECSResolvedConfiguration
from .ecs_service_connect_configuration import ECSServiceConnectConfiguration
from .ecs_service_registry import ECSServiceRegistry
from .ecs_service_revision_overrides import ECSServiceRevisionOverrides
from .ecs_service_volume_configuration import ECSServiceVolumeConfiguration
from .ecs_vpc_lattice_configuration import ECSVpcLatticeConfiguration


class ECSServiceRevision(BaseModel):
    serviceRevisionArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    taskDefinition: StrictStr | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    launchType: StrictStr | None = None
    platformVersion: StrictStr | None = None
    platformFamily: StrictStr | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    containerImages: list[ECSContainerImage] | None = None
    guardDutyEnabled: StrictBool | None = None
    serviceConnectConfiguration: ECSServiceConnectConfiguration | None = None
    volumeConfigurations: list[ECSServiceVolumeConfiguration] | None = None
    fargateEphemeralStorage: ECSDeploymentEphemeralStorage | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    vpcLatticeConfigurations: list[ECSVpcLatticeConfiguration] | None = None
    resolvedConfiguration: ECSResolvedConfiguration | None = None
    ecsManagedResources: ECSManagedResources | None = None
    overrides: ECSServiceRevisionOverrides | None = None
    gatewayConnectors: list[ECSGatewayConnector] | None = None
    monitoring: ECSMonitoringConfiguration | None = None
