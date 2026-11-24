from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_egress_only_internet_gateway import EC2EgressOnlyInternetGateway


class EC2DescribeEgressOnlyInternetGatewaysResponse(BaseModel):
    EgressOnlyInternetGateways: list[EC2EgressOnlyInternetGateway] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
