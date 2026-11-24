from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCodeRepositoryDetails(BaseModel):
    ProviderType: StrictStr | None = None
    ProjectName: StrictStr | None = None
    CodeSecurityIntegrationArn: StrictStr | None = None
