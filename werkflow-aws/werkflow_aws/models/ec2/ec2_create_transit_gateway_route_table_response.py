from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_route_table import EC2TransitGatewayRouteTable


class EC2CreateTransitGatewayRouteTableResponse(BaseModel):
    TransitGatewayRouteTable: EC2TransitGatewayRouteTable | None = None
    ResponseMetadata: dict[str, Any] | None = None
