from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails(BaseModel):
    ContainerPath: StrictStr | None = None
    HostPath: StrictStr | None = None
    Permissions: list[StrictStr] | None = None
