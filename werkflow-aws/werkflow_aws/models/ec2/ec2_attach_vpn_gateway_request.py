from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AttachVpnGatewayRequest(BaseModel):
    VpcId: StrictStr
    VpnGatewayId: StrictStr
    DryRun: StrictBool | None = None
