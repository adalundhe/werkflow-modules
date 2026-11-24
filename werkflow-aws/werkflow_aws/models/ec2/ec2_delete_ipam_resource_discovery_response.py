from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_resource_discovery import EC2IpamResourceDiscovery


class EC2DeleteIpamResourceDiscoveryResponse(BaseModel):
    IpamResourceDiscovery: EC2IpamResourceDiscovery | None = None
    ResponseMetadata: dict[str, Any] | None = None
