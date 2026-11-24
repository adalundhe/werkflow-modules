from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_network_header import SecurityHubNetworkHeader


class SecurityHubNetworkPathComponent(BaseModel):
    ComponentId: StrictStr | None = None
    ComponentType: StrictStr | None = None
    Egress: SecurityHubNetworkHeader | None = None
    Ingress: SecurityHubNetworkHeader | None = None
