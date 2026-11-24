from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpnConnectionRequest(BaseModel):
    VpnConnectionId: StrictStr
    DryRun: StrictBool | None = None
