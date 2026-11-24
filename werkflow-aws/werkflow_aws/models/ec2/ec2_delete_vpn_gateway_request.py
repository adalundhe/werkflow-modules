from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpnGatewayRequest(BaseModel):
    VpnGatewayId: StrictStr
    DryRun: StrictBool | None = None
