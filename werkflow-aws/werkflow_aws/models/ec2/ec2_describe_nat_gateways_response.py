from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_nat_gateway import EC2NatGateway


class EC2DescribeNatGatewaysResponse(BaseModel):
    NatGateways: list[EC2NatGateway] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
