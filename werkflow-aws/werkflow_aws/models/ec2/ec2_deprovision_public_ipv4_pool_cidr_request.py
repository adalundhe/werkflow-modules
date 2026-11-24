from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeprovisionPublicIpv4PoolCidrRequest(BaseModel):
    PoolId: StrictStr
    Cidr: StrictStr
    DryRun: StrictBool | None = None
