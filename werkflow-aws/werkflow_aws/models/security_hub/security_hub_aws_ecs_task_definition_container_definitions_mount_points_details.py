from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails(BaseModel):
    ContainerPath: StrictStr | None = None
    ReadOnly: StrictBool | None = None
    SourceVolume: StrictStr | None = None
