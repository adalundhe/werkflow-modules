from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_propagation import EC2TransitGatewayPropagation


class EC2EnableTransitGatewayRouteTablePropagationResponse(BaseModel):
    Propagation: EC2TransitGatewayPropagation | None = None
    ResponseMetadata: dict[str, Any] | None = None
