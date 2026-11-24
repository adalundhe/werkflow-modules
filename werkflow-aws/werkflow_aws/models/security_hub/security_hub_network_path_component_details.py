from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_port_range import SecurityHubPortRange


class SecurityHubNetworkPathComponentDetails(BaseModel):
    Address: list[StrictStr] | None = None
    PortRanges: list[SecurityHubPortRange] | None = None
