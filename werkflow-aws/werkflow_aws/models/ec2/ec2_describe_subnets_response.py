from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_subnet import EC2Subnet


class EC2DescribeSubnetsResponse(BaseModel):
    Subnets: list[EC2Subnet] | None = None
    NextToken: StrictStr | None = None
