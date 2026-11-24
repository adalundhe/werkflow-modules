from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_pool_allocation import EC2IpamPoolAllocation


class EC2DescribeIpamPoolAllocationsResponse(BaseModel):
    IpamPoolAllocations: list[EC2IpamPoolAllocation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
