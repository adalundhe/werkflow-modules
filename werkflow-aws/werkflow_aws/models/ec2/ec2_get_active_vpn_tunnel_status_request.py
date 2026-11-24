from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetActiveVpnTunnelStatusRequest(BaseModel):
    VpnConnectionId: StrictStr
    VpnTunnelOutsideIpAddress: StrictStr
    DryRun: StrictBool | None = None
