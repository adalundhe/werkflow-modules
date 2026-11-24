from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_azure_scope_configuration import SecurityHubAzureScopeConfiguration


class SecurityHubAzureDetail(BaseModel):
    AWSConfigConnectorArn: StrictStr | None = None
    ScopeConfiguration: SecurityHubAzureScopeConfiguration | None = None
    AzureRegions: list[StrictStr] | None = None
