from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_security_hub_configuration import MacieSecurityHubConfiguration


class MacieGetFindingsPublicationConfigurationResponse(BaseModel):
    securityHubConfiguration: MacieSecurityHubConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
