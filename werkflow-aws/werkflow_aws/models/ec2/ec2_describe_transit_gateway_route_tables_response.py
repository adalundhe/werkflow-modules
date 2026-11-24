from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_route_table import EC2TransitGatewayRouteTable


class EC2DescribeTransitGatewayRouteTablesResponse(BaseModel):
    TransitGatewayRouteTables: list[EC2TransitGatewayRouteTable] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
