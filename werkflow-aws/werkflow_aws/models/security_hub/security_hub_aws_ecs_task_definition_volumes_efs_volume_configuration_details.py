from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details import SecurityHubAwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails


class SecurityHubAwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails(BaseModel):
    AuthorizationConfig: SecurityHubAwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails | None = None
    FilesystemId: StrictStr | None = None
    RootDirectory: StrictStr | None = None
    TransitEncryption: StrictStr | None = None
    TransitEncryptionPort: StrictInt | None = None
