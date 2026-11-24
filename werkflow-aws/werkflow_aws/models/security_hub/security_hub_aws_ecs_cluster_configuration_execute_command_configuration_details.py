from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details import SecurityHubAwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails


class SecurityHubAwsEcsClusterConfigurationExecuteCommandConfigurationDetails(BaseModel):
    KmsKeyId: StrictStr | None = None
    LogConfiguration: SecurityHubAwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails | None = None
    Logging: StrictStr | None = None
