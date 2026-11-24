from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails(BaseModel):
    Options: dict[StrictStr, StrictStr] | None = None
    Type: StrictStr | None = None
