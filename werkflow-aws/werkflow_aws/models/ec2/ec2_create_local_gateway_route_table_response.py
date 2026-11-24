from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_route_table import EC2LocalGatewayRouteTable


class EC2CreateLocalGatewayRouteTableResponse(BaseModel):
    LocalGatewayRouteTable: EC2LocalGatewayRouteTable | None = None
    ResponseMetadata: dict[str, Any] | None = None
