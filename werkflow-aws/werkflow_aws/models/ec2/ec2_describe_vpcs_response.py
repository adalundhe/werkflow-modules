from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_vpc import EC2Vpc


class EC2DescribeVpcsResponse(BaseModel):
    Vpcs: list[EC2Vpc] | None = None
    NextToken: StrictStr | None = None
