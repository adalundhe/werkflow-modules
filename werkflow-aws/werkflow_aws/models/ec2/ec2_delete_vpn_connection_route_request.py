from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DeleteVpnConnectionRouteRequest(BaseModel):
    DestinationCidrBlock: StrictStr
    VpnConnectionId: StrictStr
