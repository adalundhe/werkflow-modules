from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_route_server_peer import EC2RouteServerPeer


class EC2DeleteRouteServerPeerResponse(BaseModel):
    RouteServerPeer: EC2RouteServerPeer | None = None
    ResponseMetadata: dict[str, Any] | None = None
