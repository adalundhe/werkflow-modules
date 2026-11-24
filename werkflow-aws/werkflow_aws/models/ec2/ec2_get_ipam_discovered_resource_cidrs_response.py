from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_discovered_resource_cidr import EC2IpamDiscoveredResourceCidr


class EC2GetIpamDiscoveredResourceCidrsResponse(BaseModel):
    IpamDiscoveredResourceCidrs: list[EC2IpamDiscoveredResourceCidr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
