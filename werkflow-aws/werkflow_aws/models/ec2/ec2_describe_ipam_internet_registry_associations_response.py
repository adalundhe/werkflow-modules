from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_internet_registry_association import EC2IpamInternetRegistryAssociation


class EC2DescribeIpamInternetRegistryAssociationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamInternetRegistryAssociations: list[EC2IpamInternetRegistryAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
