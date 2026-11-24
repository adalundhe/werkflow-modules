from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_discovered_route import EC2IpamDiscoveredRoute


class EC2GetIpamDiscoveredRoutesResponse(BaseModel):
    IpamDiscoveredRoutes: list[EC2IpamDiscoveredRoute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
