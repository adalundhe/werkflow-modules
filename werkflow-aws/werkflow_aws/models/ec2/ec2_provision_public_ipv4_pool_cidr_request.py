from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ProvisionPublicIpv4PoolCidrRequest(BaseModel):
    IpamPoolId: StrictStr
    PoolId: StrictStr
    NetmaskLength: StrictInt
    DryRun: StrictBool | None = None
    NetworkBorderGroup: StrictStr | None = None
