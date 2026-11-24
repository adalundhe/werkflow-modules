from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_route_server_propagation import EC2RouteServerPropagation


class EC2GetRouteServerPropagationsResponse(BaseModel):
    RouteServerPropagations: list[EC2RouteServerPropagation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
