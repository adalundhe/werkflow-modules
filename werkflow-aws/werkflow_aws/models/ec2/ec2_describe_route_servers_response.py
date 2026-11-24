from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_route_server import EC2RouteServer


class EC2DescribeRouteServersResponse(BaseModel):
    RouteServers: list[EC2RouteServer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
