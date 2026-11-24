from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_resource_discovery import EC2IpamResourceDiscovery


class EC2DescribeIpamResourceDiscoveriesResponse(BaseModel):
    IpamResourceDiscoveries: list[EC2IpamResourceDiscovery] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
