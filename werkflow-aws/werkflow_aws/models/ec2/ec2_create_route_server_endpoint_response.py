from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_route_server_endpoint import EC2RouteServerEndpoint


class EC2CreateRouteServerEndpointResponse(BaseModel):
    RouteServerEndpoint: EC2RouteServerEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
