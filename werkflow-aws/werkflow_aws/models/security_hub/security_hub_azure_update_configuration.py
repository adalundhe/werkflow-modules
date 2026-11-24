from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_azure_scope_configuration import SecurityHubAzureScopeConfiguration


class SecurityHubAzureUpdateConfiguration(BaseModel):
    ScopeConfiguration: SecurityHubAzureScopeConfiguration
    AzureRegions: list[StrictStr]
