from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails(BaseModel):
    Name: StrictStr | None = None
    ValueFrom: StrictStr | None = None
