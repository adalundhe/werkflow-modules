from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_resource_cidr import EC2IpamResourceCidr


class EC2ModifyIpamResourceCidrResponse(BaseModel):
    IpamResourceCidr: EC2IpamResourceCidr | None = None
    ResponseMetadata: dict[str, Any] | None = None
