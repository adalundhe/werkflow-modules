from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_provider_configuration import SecurityHubProviderConfiguration


class SecurityHubCreateConnectorV2Request(BaseModel):
    Name: StrictStr
    Provider: SecurityHubProviderConfiguration
    Description: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
