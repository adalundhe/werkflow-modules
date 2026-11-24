from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeprovisionIpamPoolCidrRequest(BaseModel):
    IpamPoolId: StrictStr
    DryRun: StrictBool | None = None
    Cidr: StrictStr | None = None
