from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_provider_detail import SecurityHubProviderDetail


class SecurityHubProviderSummary(BaseModel):
    ProviderName: StrictStr | None = None
    ConnectorStatus: StrictStr | None = None
    ProviderConfiguration: SecurityHubProviderDetail | None = None
