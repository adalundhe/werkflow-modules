from __future__ import annotations
from pydantic import BaseModel
from .security_hub_action_local_ip_details import SecurityHubActionLocalIpDetails
from .security_hub_action_local_port_details import SecurityHubActionLocalPortDetails
from .security_hub_action_remote_ip_details import SecurityHubActionRemoteIpDetails


class SecurityHubPortProbeDetail(BaseModel):
    LocalPortDetails: SecurityHubActionLocalPortDetails | None = None
    LocalIpDetails: SecurityHubActionLocalIpDetails | None = None
    RemoteIpDetails: SecurityHubActionRemoteIpDetails | None = None
