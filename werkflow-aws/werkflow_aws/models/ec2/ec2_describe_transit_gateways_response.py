from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway import EC2TransitGateway


class EC2DescribeTransitGatewaysResponse(BaseModel):
    TransitGateways: list[EC2TransitGateway] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
