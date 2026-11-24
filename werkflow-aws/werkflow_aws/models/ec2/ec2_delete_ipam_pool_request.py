from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamPoolRequest(BaseModel):
    IpamPoolId: StrictStr
    DryRun: StrictBool | None = None
    Cascade: StrictBool | None = None
