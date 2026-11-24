from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCodeBuildProjectEnvironmentRegistryCredential(BaseModel):
    Credential: StrictStr | None = None
    CredentialProvider: StrictStr | None = None
