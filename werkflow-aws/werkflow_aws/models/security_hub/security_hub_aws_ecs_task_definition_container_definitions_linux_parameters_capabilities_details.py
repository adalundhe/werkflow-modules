from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails(BaseModel):
    Add: list[StrictStr] | None = None
    Drop: list[StrictStr] | None = None
