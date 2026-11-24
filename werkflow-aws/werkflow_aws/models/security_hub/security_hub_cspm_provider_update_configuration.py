from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_update_configuration import SecurityHubAzureUpdateConfiguration
from .security_hub_gcp_update_configuration import SecurityHubGcpUpdateConfiguration


class SecurityHubCspmProviderUpdateConfiguration(BaseModel):
    Azure: SecurityHubAzureUpdateConfiguration | None = None
    GCP: SecurityHubGcpUpdateConfiguration | None = None
