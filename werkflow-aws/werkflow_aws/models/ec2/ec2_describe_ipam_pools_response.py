from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_pool import EC2IpamPool


class EC2DescribeIpamPoolsResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamPools: list[EC2IpamPool] | None = None
    ResponseMetadata: dict[str, Any] | None = None
