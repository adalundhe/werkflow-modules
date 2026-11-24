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
from .ecs_tag import ECSTag
from .ecs_vpc_lattice_configuration import ECSVpcLatticeConfiguration


class ECSCreateServiceRequest(BaseModel):
    serviceName: StrictStr
    cluster: StrictStr | None = None
    taskDefinition: StrictStr | None = None
    availabilityZoneRebalancing: Literal['ENABLED', 'DISABLED'] | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    desiredCount: StrictInt | None = None
    clientToken: StrictStr | None = None
    launchType: Literal['EC2', 'FARGATE', 'EXTERNAL', 'MANAGED_INSTANCES'] | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    platformVersion: StrictStr | None = None
    role: StrictStr | None = None
    deploymentConfiguration: ECSDeploymentConfiguration | None = None
    placementConstraints: list[ECSPlacementConstraint] | None = None
    placementStrategy: list[ECSPlacementStrategy] | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    healthCheckGracePeriodSeconds: StrictInt | None = None
    schedulingStrategy: Literal['REPLICA', 'DAEMON'] | None = None
    deploymentController: ECSDeploymentController | None = None
    tags: list[ECSTag] | None = None
    enableECSManagedTags: StrictBool | None = None
    propagateTags: Literal['TASK_DEFINITION', 'SERVICE', 'NONE'] | None = None
    enableExecuteCommand: StrictBool | None = None
    serviceConnectConfiguration: ECSServiceConnectConfiguration | None = None
    volumeConfigurations: list[ECSServiceVolumeConfiguration] | None = None
    vpcLatticeConfigurations: list[ECSVpcLatticeConfiguration] | None = None
    gatewayConnectors: list[ECSGatewayConnector] | None = None
    monitoring: ECSMonitoringConfiguration | None = None
