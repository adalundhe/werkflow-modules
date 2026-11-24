from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_capacity_provider_strategy_item import ECSCapacityProviderStrategyItem
from .ecs_deployment import ECSDeployment
from .ecs_deployment_configuration import ECSDeploymentConfiguration
from .ecs_deployment_controller import ECSDeploymentController
from .ecs_load_balancer import ECSLoadBalancer
from .ecs_network_configuration import ECSNetworkConfiguration
from .ecs_placement_constraint import ECSPlacementConstraint
from .ecs_placement_strategy import ECSPlacementStrategy
from .ecs_service_current_revision_summary import ECSServiceCurrentRevisionSummary
from .ecs_service_event import ECSServiceEvent
from .ecs_service_registry import ECSServiceRegistry
from .ecs_tag import ECSTag
from .ecs_task_set import ECSTaskSet


class ECSService(BaseModel):
    serviceArn: StrictStr | None = None
    serviceName: StrictStr | None = None
    clusterArn: StrictStr | None = None
    loadBalancers: list[ECSLoadBalancer] | None = None
    serviceRegistries: list[ECSServiceRegistry] | None = None
    status: StrictStr | None = None
    desiredCount: StrictInt | None = None
    runningCount: StrictInt | None = None
    pendingCount: StrictInt | None = None
    launchType: StrictStr | None = None
    capacityProviderStrategy: list[ECSCapacityProviderStrategyItem] | None = None
    platformVersion: StrictStr | None = None
    platformFamily: StrictStr | None = None
    taskDefinition: StrictStr | None = None
    deploymentConfiguration: ECSDeploymentConfiguration | None = None
    taskSets: list[ECSTaskSet] | None = None
    deployments: list[ECSDeployment] | None = None
    roleArn: StrictStr | None = None
    events: list[ECSServiceEvent] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    currentServiceDeployment: StrictStr | None = None
    currentServiceRevisions: list[ECSServiceCurrentRevisionSummary] | None = None
    placementConstraints: list[ECSPlacementConstraint] | None = None
    placementStrategy: list[ECSPlacementStrategy] | None = None
    networkConfiguration: ECSNetworkConfiguration | None = None
    healthCheckGracePeriodSeconds: StrictInt | None = None
    schedulingStrategy: StrictStr | None = None
    deploymentController: ECSDeploymentController | None = None
    tags: list[ECSTag] | None = None
    createdBy: StrictStr | None = None
    enableECSManagedTags: StrictBool | None = None
    propagateTags: StrictStr | None = None
    enableExecuteCommand: StrictBool | None = None
    availabilityZoneRebalancing: StrictStr | None = None
    resourceManagementType: StrictStr | None = None
