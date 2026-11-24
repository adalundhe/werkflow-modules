from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_route_table import EC2RouteTable


class EC2DescribeRouteTablesResponse(BaseModel):
    RouteTables: list[EC2RouteTable] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
