from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_azure_scope_configuration import SecurityHubAzureScopeConfiguration


class SecurityHubAzureProviderConfiguration(BaseModel):
    AWSConfigConnectorArn: StrictStr
    ScopeConfiguration: SecurityHubAzureScopeConfiguration
    AzureRegions: list[StrictStr]
