from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyIpamPoolAllocationRequest(BaseModel):
    IpamPoolAllocationId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
