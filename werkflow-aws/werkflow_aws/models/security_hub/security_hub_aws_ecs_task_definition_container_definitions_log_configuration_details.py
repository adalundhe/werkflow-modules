from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_task_definition_container_definitions_log_configuration_secret_options_details import SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails(BaseModel):
    LogDriver: StrictStr | None = None
    Options: dict[StrictStr, StrictStr] | None = None
    SecretOptions: list[SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails] | None = None
