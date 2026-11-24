from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetVpnTunnelReplacementStatusRequest(BaseModel):
    VpnConnectionId: StrictStr
    VpnTunnelOutsideIpAddress: StrictStr
    DryRun: StrictBool | None = None
