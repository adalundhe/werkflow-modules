from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipv6_pool import EC2Ipv6Pool


class EC2DescribeIpv6PoolsResponse(BaseModel):
    Ipv6Pools: list[EC2Ipv6Pool] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
