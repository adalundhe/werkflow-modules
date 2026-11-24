from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_route_server import EC2RouteServer


class EC2DeleteRouteServerResponse(BaseModel):
    RouteServer: EC2RouteServer | None = None
    ResponseMetadata: dict[str, Any] | None = None
