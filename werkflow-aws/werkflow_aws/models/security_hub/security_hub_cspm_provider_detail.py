from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_detail import SecurityHubAzureDetail
from .security_hub_gcp_detail import SecurityHubGcpDetail


class SecurityHubCspmProviderDetail(BaseModel):
    Azure: SecurityHubAzureDetail | None = None
    GCP: SecurityHubGcpDetail | None = None
