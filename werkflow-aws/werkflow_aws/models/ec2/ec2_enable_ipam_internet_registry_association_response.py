from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_internet_registry_association import EC2IpamInternetRegistryAssociation


class EC2EnableIpamInternetRegistryAssociationResponse(BaseModel):
    IpamInternetRegistryAssociation: EC2IpamInternetRegistryAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
