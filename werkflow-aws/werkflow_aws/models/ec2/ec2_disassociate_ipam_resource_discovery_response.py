from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_resource_discovery_association import EC2IpamResourceDiscoveryAssociation


class EC2DisassociateIpamResourceDiscoveryResponse(BaseModel):
    IpamResourceDiscoveryAssociation: EC2IpamResourceDiscoveryAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
