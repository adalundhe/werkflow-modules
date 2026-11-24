from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ecs_task_definition_container_definitions_depends_on_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails
from .security_hub_aws_ecs_task_definition_container_definitions_environment_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails
from .security_hub_aws_ecs_task_definition_container_definitions_environment_files_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails
from .security_hub_aws_ecs_task_definition_container_definitions_extra_hosts_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_firelens_configuration_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails
from .security_hub_aws_ecs_task_definition_container_definitions_health_check_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails
from .security_hub_aws_ecs_task_definition_container_definitions_linux_parameters_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails
from .security_hub_aws_ecs_task_definition_container_definitions_log_configuration_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails
from .security_hub_aws_ecs_task_definition_container_definitions_mount_points_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_port_mappings_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_repository_credentials_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_resource_requirements_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_secrets_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsSecretsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_system_controls_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_ulimits_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails
from .security_hub_aws_ecs_task_definition_container_definitions_volumes_from_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDetails(BaseModel):
    Command: list[StrictStr] | None = None
    Cpu: StrictInt | None = None
    DependsOn: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails] | None = None
    DisableNetworking: StrictBool | None = None
    DnsSearchDomains: list[StrictStr] | None = None
    DnsServers: list[StrictStr] | None = None
    DockerLabels: dict[StrictStr, StrictStr] | None = None
    DockerSecurityOptions: list[StrictStr] | None = None
    EntryPoint: list[StrictStr] | None = None
    Environment: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails] | None = None
    EnvironmentFiles: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails] | None = None
    Essential: StrictBool | None = None
    ExtraHosts: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails] | None = None
    FirelensConfiguration: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails | None = None
    HealthCheck: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails | None = None
    Hostname: StrictStr | None = None
    Image: StrictStr | None = None
    Interactive: StrictBool | None = None
    Links: list[StrictStr] | None = None
    LinuxParameters: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails | None = None
    LogConfiguration: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails | None = None
    Memory: StrictInt | None = None
    MemoryReservation: StrictInt | None = None
    MountPoints: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails] | None = None
    Name: StrictStr | None = None
    PortMappings: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails] | None = None
    Privileged: StrictBool | None = None
    PseudoTerminal: StrictBool | None = None
    ReadonlyRootFilesystem: StrictBool | None = None
    RepositoryCredentials: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails | None = None
    ResourceRequirements: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails] | None = None
    Secrets: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsSecretsDetails] | None = None
    StartTimeout: StrictInt | None = None
    StopTimeout: StrictInt | None = None
    SystemControls: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails] | None = None
    Ulimits: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails] | None = None
    User: StrictStr | None = None
    VolumesFrom: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails] | None = None
    WorkingDirectory: StrictStr | None = None
