from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_classic_link import EC2VpcClassicLink


class EC2DescribeVpcClassicLinkResponse(BaseModel):
    Vpcs: list[EC2VpcClassicLink] | None = None
    ResponseMetadata: dict[str, Any] | None = None
