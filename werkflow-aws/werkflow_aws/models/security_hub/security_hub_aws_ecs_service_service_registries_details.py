from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsServiceServiceRegistriesDetails(BaseModel):
    ContainerName: StrictStr | None = None
    ContainerPort: StrictInt | None = None
    Port: StrictInt | None = None
    RegistryArn: StrictStr | None = None
