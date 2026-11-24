from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails(BaseModel):
    HardLimit: StrictInt | None = None
    Name: StrictStr | None = None
    SoftLimit: StrictInt | None = None
