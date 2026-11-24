from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_deployment_configuration import ECSDeploymentConfiguration
from .ecs_deployment_controller import ECSDeploymentController
from .ecs_gateway_connector import ECSGatewayConnector
from .ecs_load_balancer import ECSLoadBalancer
from .ecs_monitoring_configuration import ECSMonitoringConfiguration
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_placement_constraint import ECSPlacementConstraint
from .ecs_placement_strategy import ECSPlacementStrategy
from .ecs_service_connect_configuration import ECSServiceConnectConfiguration
from .ecs_service_registry import ECSServiceRegistry
from .ecs_service_volume_configuration import ECSServiceVolumeConfiguration
from .ecs_vpc_lattice_configuration import ECSVpcLatticeConfiguration


class ECSUpdateServiceRequest(BaseModel):
    service: StrictStr
    cluster: StrictStr | None = None
    desiredCount: StrictInt | None = None
    taskDefinition: StrictStr | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    deploymentConfiguration: ECSDeploymentConfiguration | None = None
    availabilityZoneRebalancing: Literal['ENABLED', 'DISABLED'] | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    placementConstraints: list[ECSPlacementConstraint] | None = None
    placementStrategy: list[ECSPlacementStrategy] | None = None
    platformVersion: StrictStr | None = None
    forceNewDeployment: StrictBool | None = None
    healthCheckGracePeriodSeconds: StrictInt | None = None
    deploymentController: ECSDeploymentController | None = None
    enableExecuteCommand: StrictBool | None = None
    enableECSManagedTags: StrictBool | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    propagateTags: Literal['TASK_DEFINITION', 'SERVICE', 'NONE'] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    serviceConnectConfiguration: ECSServiceConnectConfiguration | None = None
    volumeConfigurations: list[ECSServiceVolumeConfiguration] | None = None
    vpcLatticeConfigurations: list[ECSVpcLatticeConfiguration] | None = None
    gatewayConnectors: list[ECSGatewayConnector] | None = None
    monitoring: ECSMonitoringConfiguration | None = None
