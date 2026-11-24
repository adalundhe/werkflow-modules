from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamPrefixListResolverTargetRequest(BaseModel):
    IpamPrefixListResolverTargetId: StrictStr
    DryRun: StrictBool | None = None
