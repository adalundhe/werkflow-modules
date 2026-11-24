from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_metering_policy import EC2TransitGatewayMeteringPolicy


class EC2DescribeTransitGatewayMeteringPoliciesResponse(BaseModel):
    TransitGatewayMeteringPolicies: list[EC2TransitGatewayMeteringPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
