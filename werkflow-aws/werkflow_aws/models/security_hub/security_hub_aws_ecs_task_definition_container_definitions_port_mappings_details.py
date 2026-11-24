from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails(BaseModel):
    ContainerPort: StrictInt | None = None
    HostPort: StrictInt | None = None
    Protocol: StrictStr | None = None
