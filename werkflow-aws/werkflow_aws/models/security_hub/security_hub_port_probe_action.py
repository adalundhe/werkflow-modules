from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .security_hub_port_probe_detail import SecurityHubPortProbeDetail


class SecurityHubPortProbeAction(BaseModel):
    PortProbeDetails: list[SecurityHubPortProbeDetail] | None = None
    Blocked: StrictBool | None = None
