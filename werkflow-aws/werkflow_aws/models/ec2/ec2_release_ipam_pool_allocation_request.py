from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReleaseIpamPoolAllocationRequest(BaseModel):
    IpamPoolId: StrictStr
    Cidr: StrictStr
    IpamPoolAllocationId: StrictStr
    DryRun: StrictBool | None = None
