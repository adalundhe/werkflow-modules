from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_pool_allocation import EC2IpamPoolAllocation


class EC2ModifyIpamPoolAllocationResponse(BaseModel):
    IpamPoolAllocation: EC2IpamPoolAllocation | None = None
    ResponseMetadata: dict[str, Any] | None = None
