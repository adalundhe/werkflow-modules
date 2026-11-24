from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_metering_policy import EC2TransitGatewayMeteringPolicy


class EC2CreateTransitGatewayMeteringPolicyResponse(BaseModel):
    TransitGatewayMeteringPolicy: EC2TransitGatewayMeteringPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
