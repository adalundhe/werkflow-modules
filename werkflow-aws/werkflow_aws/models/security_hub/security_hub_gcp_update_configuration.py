from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_gcp_scope_configuration import SecurityHubGcpScopeConfiguration


class SecurityHubGcpUpdateConfiguration(BaseModel):
    ScopeConfiguration: SecurityHubGcpScopeConfiguration
    GCPRegions: list[StrictStr]
