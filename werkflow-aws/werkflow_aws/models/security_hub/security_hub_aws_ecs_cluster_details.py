from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_ecs_cluster_cluster_settings_details import SecurityHubAwsEcsClusterClusterSettingsDetails
from .security_hub_aws_ecs_cluster_configuration_details import SecurityHubAwsEcsClusterConfigurationDetails
from .security_hub_aws_ecs_cluster_default_capacity_provider_strategy_details import SecurityHubAwsEcsClusterDefaultCapacityProviderStrategyDetails


class SecurityHubAwsEcsClusterDetails(BaseModel):
    ClusterArn: StrictStr | None = None
    ActiveServicesCount: StrictInt | None = None
    CapacityProviders: list[StrictStr] | None = None
    ClusterSettings: list[SecurityHubAwsEcsClusterClusterSettingsDetails] | None = None
    Configuration: SecurityHubAwsEcsClusterConfigurationDetails | None = None
    DefaultCapacityProviderStrategy: list[SecurityHubAwsEcsClusterDefaultCapacityProviderStrategyDetails] | None = None
    ClusterName: StrictStr | None = None
    RegisteredContainerInstancesCount: StrictInt | None = None
    RunningTasksCount: StrictInt | None = None
    Status: StrictStr | None = None
