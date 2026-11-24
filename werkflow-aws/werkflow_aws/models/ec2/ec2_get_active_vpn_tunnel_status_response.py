from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_active_vpn_tunnel_status import EC2ActiveVpnTunnelStatus


class EC2GetActiveVpnTunnelStatusResponse(BaseModel):
    ActiveVpnTunnelStatus: EC2ActiveVpnTunnelStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
