from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_local_gateway_route_table import EC2LocalGatewayRouteTable


class EC2DescribeLocalGatewayRouteTablesResponse(BaseModel):
    LocalGatewayRouteTables: list[EC2LocalGatewayRouteTable] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
