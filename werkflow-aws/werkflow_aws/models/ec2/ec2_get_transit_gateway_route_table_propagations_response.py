from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_route_table_propagation import EC2TransitGatewayRouteTablePropagation


class EC2GetTransitGatewayRouteTablePropagationsResponse(BaseModel):
    TransitGatewayRouteTablePropagations: list[EC2TransitGatewayRouteTablePropagation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
