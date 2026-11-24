from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_public_ipv4_pool import EC2PublicIpv4Pool


class EC2DescribePublicIpv4PoolsResponse(BaseModel):
    PublicIpv4Pools: list[EC2PublicIpv4Pool] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
