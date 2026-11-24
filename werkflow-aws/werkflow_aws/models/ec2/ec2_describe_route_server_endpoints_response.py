from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_route_server_endpoint import EC2RouteServerEndpoint


class EC2DescribeRouteServerEndpointsResponse(BaseModel):
    RouteServerEndpoints: list[EC2RouteServerEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
