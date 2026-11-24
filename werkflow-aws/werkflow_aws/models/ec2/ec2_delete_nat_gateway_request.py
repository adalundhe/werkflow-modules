from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNatGatewayRequest(BaseModel):
    NatGatewayId: StrictStr
    DryRun: StrictBool | None = None
