from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_internet_registry_association_cidr import EC2IpamInternetRegistryAssociationCidr


class EC2GetIpamInternetRegistryAssociationCidrsResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamInternetRegistryAssociationCidrs: list[EC2IpamInternetRegistryAssociationCidr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
