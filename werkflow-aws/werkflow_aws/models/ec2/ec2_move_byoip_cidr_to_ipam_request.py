from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2MoveByoipCidrToIpamRequest(BaseModel):
    Cidr: StrictStr
    IpamPoolId: StrictStr
    IpamPoolOwner: StrictStr
    DryRun: StrictBool | None = None
