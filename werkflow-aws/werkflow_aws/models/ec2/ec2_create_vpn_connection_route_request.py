from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CreateVpnConnectionRouteRequest(BaseModel):
    DestinationCidrBlock: StrictStr
    VpnConnectionId: StrictStr
