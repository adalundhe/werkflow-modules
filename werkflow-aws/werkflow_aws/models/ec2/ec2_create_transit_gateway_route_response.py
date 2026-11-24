from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_route import EC2TransitGatewayRoute


class EC2CreateTransitGatewayRouteResponse(BaseModel):
    Route: EC2TransitGatewayRoute | None = None
    ResponseMetadata: dict[str, Any] | None = None
