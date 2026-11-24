from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReplaceVpnTunnelRequest(BaseModel):
    VpnConnectionId: StrictStr
    VpnTunnelOutsideIpAddress: StrictStr
    ApplyPendingMaintenance: StrictBool | None = None
    DryRun: StrictBool | None = None
