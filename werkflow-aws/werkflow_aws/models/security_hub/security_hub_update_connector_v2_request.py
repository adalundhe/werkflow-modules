from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_provider_update_configuration import SecurityHubProviderUpdateConfiguration


class SecurityHubUpdateConnectorV2Request(BaseModel):
    ConnectorId: StrictStr
    Description: StrictStr | None = None
    Provider: SecurityHubProviderUpdateConfiguration | None = None
