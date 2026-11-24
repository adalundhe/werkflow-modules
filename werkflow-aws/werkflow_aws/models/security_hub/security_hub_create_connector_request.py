from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_provider_configuration import SecurityHubCspmProviderConfiguration


class SecurityHubCreateConnectorRequest(BaseModel):
    Name: StrictStr
    Provider: SecurityHubCspmProviderConfiguration
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
