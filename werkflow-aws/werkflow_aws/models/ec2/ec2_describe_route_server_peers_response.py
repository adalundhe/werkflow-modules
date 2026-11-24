from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_route_server_peer import EC2RouteServerPeer


class EC2DescribeRouteServerPeersResponse(BaseModel):
    RouteServerPeers: list[EC2RouteServerPeer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
