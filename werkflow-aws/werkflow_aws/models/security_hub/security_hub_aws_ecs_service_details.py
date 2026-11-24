from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ecs_service_capacity_provider_strategy_details import SecurityHubAwsEcsServiceCapacityProviderStrategyDetails
from .security_hub_aws_ecs_service_deployment_configuration_details import SecurityHubAwsEcsServiceDeploymentConfigurationDetails
from .security_hub_aws_ecs_service_deployment_controller_details import SecurityHubAwsEcsServiceDeploymentControllerDetails
from .security_hub_aws_ecs_service_load_balancers_details import SecurityHubAwsEcsServiceLoadBalancersDetails
from .security_hub_aws_ecs_service_network_configuration_details import SecurityHubAwsEcsServiceNetworkConfigurationDetails
from .security_hub_aws_ecs_service_placement_constraints_details import SecurityHubAwsEcsServicePlacementConstraintsDetails
from .security_hub_aws_ecs_service_placement_strategies_details import SecurityHubAwsEcsServicePlacementStrategiesDetails
from .security_hub_aws_ecs_service_service_registries_details import SecurityHubAwsEcsServiceServiceRegistriesDetails


class SecurityHubAwsEcsServiceDetails(BaseModel):
    CapacityProviderStrategy: list[SecurityHubAwsEcsServiceCapacityProviderStrategyDetails] | None = None
    Cluster: StrictStr | None = None
    DeploymentConfiguration: SecurityHubAwsEcsServiceDeploymentConfigurationDetails | None = None
    DeploymentController: SecurityHubAwsEcsServiceDeploymentControllerDetails | None = None
    DesiredCount: StrictInt | None = None
    EnableEcsManagedTags: StrictBool | None = None
    EnableExecuteCommand: StrictBool | None = None
    HealthCheckGracePeriodSeconds: StrictInt | None = None
    LaunchType: StrictStr | None = None
    LoadBalancers: list[SecurityHubAwsEcsServiceLoadBalancersDetails] | None = None
    Name: StrictStr | None = None
    NetworkConfiguration: SecurityHubAwsEcsServiceNetworkConfigurationDetails | None = None
    PlacementConstraints: list[SecurityHubAwsEcsServicePlacementConstraintsDetails] | None = None
    PlacementStrategies: list[SecurityHubAwsEcsServicePlacementStrategiesDetails] | None = None
    PlatformVersion: StrictStr | None = None
    PropagateTags: StrictStr | None = None
    Role: StrictStr | None = None
    SchedulingStrategy: StrictStr | None = None
    ServiceArn: StrictStr | None = None
    ServiceName: StrictStr | None = None
    ServiceRegistries: list[SecurityHubAwsEcsServiceServiceRegistriesDetails] | None = None
    TaskDefinition: StrictStr | None = None
