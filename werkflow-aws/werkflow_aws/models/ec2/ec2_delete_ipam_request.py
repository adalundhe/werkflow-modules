from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamRequest(BaseModel):
    IpamId: StrictStr
    DryRun: StrictBool | None = None
    Cascade: StrictBool | None = None
