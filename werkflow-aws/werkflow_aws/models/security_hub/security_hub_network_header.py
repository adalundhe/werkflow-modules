from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_network_path_component_details import SecurityHubNetworkPathComponentDetails


class SecurityHubNetworkHeader(BaseModel):
    Protocol: StrictStr | None = None
    Destination: SecurityHubNetworkPathComponentDetails | None = None
    Source: SecurityHubNetworkPathComponentDetails | None = None
