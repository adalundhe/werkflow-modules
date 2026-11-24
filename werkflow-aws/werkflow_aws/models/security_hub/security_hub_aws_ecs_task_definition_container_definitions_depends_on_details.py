from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails(BaseModel):
    Condition: StrictStr | None = None
    ContainerName: StrictStr | None = None
