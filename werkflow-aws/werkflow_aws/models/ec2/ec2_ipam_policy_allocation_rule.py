from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamPolicyAllocationRule(BaseModel):
    SourceIpamPoolId: StrictStr | None = None
