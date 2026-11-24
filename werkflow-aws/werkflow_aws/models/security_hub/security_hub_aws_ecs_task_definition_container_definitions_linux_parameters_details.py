from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .security_hub_aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails
from .security_hub_aws_ecs_task_definition_container_definitions_linux_parameters_devices_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails
from .security_hub_aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails(BaseModel):
    Capabilities: SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails | None = None
    Devices: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails] | None = None
    InitProcessEnabled: StrictBool | None = None
    MaxSwap: StrictInt | None = None
    SharedMemorySize: StrictInt | None = None
    Swappiness: StrictInt | None = None
    Tmpfs: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails] | None = None
