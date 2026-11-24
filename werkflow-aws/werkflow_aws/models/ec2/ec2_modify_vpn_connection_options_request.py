from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpnConnectionOptionsRequest(BaseModel):
    VpnConnectionId: StrictStr
    LocalIpv4NetworkCidr: StrictStr | None = None
    RemoteIpv4NetworkCidr: StrictStr | None = None
    LocalIpv6NetworkCidr: StrictStr | None = None
    RemoteIpv6NetworkCidr: StrictStr | None = None
    TunnelBandwidth: Literal['standard', 'large'] | None = None
    DryRun: StrictBool | None = None
