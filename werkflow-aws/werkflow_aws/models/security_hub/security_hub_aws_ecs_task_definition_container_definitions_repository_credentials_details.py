from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails(BaseModel):
    CredentialsParameter: StrictStr | None = None
