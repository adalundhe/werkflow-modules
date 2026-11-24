from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_connect import EC2TransitGatewayConnect


class EC2DescribeTransitGatewayConnectsResponse(BaseModel):
    TransitGatewayConnects: list[EC2TransitGatewayConnect] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
