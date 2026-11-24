from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamPolicyRequest(BaseModel):
    IpamPolicyId: StrictStr
    DryRun: StrictBool | None = None
