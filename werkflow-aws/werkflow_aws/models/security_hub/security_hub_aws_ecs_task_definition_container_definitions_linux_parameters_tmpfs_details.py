from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails(BaseModel):
    ContainerPath: StrictStr | None = None
    MountOptions: list[StrictStr] | None = None
    Size: StrictInt | None = None
