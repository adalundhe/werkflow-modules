from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_action_local_port_details import SecurityHubActionLocalPortDetails
from .security_hub_action_remote_ip_details import SecurityHubActionRemoteIpDetails
from .security_hub_action_remote_port_details import SecurityHubActionRemotePortDetails


class SecurityHubNetworkConnectionAction(BaseModel):
    ConnectionDirection: StrictStr | None = None
    RemoteIpDetails: SecurityHubActionRemoteIpDetails | None = None
    RemotePortDetails: SecurityHubActionRemotePortDetails | None = None
    LocalPortDetails: SecurityHubActionLocalPortDetails | None = None
    Protocol: StrictStr | None = None
    Blocked: StrictBool | None = None
