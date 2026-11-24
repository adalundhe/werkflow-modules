from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_provider_update_configuration import SecurityHubCspmProviderUpdateConfiguration


class SecurityHubUpdateConnectorRequest(BaseModel):
    ConnectorId: StrictStr
    Description: StrictStr | None = None
    Provider: SecurityHubCspmProviderUpdateConfiguration | None = None
