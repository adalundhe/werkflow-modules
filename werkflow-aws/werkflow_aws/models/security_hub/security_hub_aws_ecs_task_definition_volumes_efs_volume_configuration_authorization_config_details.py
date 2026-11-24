from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails(BaseModel):
    AccessPointId: StrictStr | None = None
    Iam: StrictStr | None = None
