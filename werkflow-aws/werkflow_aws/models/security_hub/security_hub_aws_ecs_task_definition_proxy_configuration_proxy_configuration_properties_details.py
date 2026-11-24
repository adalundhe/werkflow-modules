from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
