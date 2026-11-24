from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_resource_cidr import EC2IpamResourceCidr


class EC2GetIpamResourceCidrsResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamResourceCidrs: list[EC2IpamResourceCidr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
