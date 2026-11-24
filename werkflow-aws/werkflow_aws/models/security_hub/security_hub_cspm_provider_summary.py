from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_provider_detail import SecurityHubCspmProviderDetail


class SecurityHubCspmProviderSummary(BaseModel):
    ProviderName: StrictStr | None = None
    ConnectorStatus: StrictStr | None = None
    ProviderConfiguration: SecurityHubCspmProviderDetail | None = None
