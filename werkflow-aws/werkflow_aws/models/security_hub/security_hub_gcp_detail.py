from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_gcp_scope_configuration import SecurityHubGcpScopeConfiguration


class SecurityHubGcpDetail(BaseModel):
    AWSConfigConnectorArn: StrictStr | None = None
    ScopeConfiguration: SecurityHubGcpScopeConfiguration | None = None
    GCPRegions: list[StrictStr] | None = None
