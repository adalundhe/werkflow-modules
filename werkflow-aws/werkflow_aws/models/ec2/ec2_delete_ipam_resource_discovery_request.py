from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamResourceDiscoveryRequest(BaseModel):
    IpamResourceDiscoveryId: StrictStr
    DryRun: StrictBool | None = None
