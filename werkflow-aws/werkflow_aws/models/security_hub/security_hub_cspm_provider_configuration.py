from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_provider_configuration import SecurityHubAzureProviderConfiguration
from .security_hub_gcp_provider_configuration import SecurityHubGcpProviderConfiguration


class SecurityHubCspmProviderConfiguration(BaseModel):
    Azure: SecurityHubAzureProviderConfiguration | None = None
    GCP: SecurityHubGcpProviderConfiguration | None = None
