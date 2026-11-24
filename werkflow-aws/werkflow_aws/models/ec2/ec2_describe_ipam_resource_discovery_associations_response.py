from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_resource_discovery_association import EC2IpamResourceDiscoveryAssociation


class EC2DescribeIpamResourceDiscoveryAssociationsResponse(BaseModel):
    IpamResourceDiscoveryAssociations: list[EC2IpamResourceDiscoveryAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
