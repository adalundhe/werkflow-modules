from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_internet_registry_association_asn import EC2IpamInternetRegistryAssociationAsn


class EC2GetIpamInternetRegistryAssociationAsnsResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamInternetRegistryAssociationAsns: list[EC2IpamInternetRegistryAssociationAsn] | None = None
    ResponseMetadata: dict[str, Any] | None = None
