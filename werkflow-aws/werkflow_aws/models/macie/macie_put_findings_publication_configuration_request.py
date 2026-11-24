from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_security_hub_configuration import MacieSecurityHubConfiguration


class MaciePutFindingsPublicationConfigurationRequest(BaseModel):
    clientToken: StrictStr | None = None
    securityHubConfiguration: MacieSecurityHubConfiguration | None = None
