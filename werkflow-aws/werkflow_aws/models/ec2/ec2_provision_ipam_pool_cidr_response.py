from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_pool_cidr import EC2IpamPoolCidr


class EC2ProvisionIpamPoolCidrResponse(BaseModel):
    IpamPoolCidr: EC2IpamPoolCidr | None = None
    ResponseMetadata: dict[str, Any] | None = None
