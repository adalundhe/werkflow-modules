from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_pool_cidr import EC2IpamPoolCidr


class EC2GetIpamPoolCidrsResponse(BaseModel):
    IpamPoolCidrs: list[EC2IpamPoolCidr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
