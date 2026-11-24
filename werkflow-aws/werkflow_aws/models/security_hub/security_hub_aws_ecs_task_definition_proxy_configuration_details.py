from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_task_definition_proxy_configuration_proxy_configuration_properties_details import SecurityHubAwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails


class SecurityHubAwsEcsTaskDefinitionProxyConfigurationDetails(BaseModel):
    ContainerName: StrictStr | None = None
    ProxyConfigurationProperties: list[SecurityHubAwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails] | None = None
    Type: StrictStr | None = None
