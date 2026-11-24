from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DetachVpnGatewayRequest(BaseModel):
    VpcId: StrictStr
    VpnGatewayId: StrictStr
    DryRun: StrictBool | None = None
