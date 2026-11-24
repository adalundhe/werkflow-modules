from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_subnet_ipv6_cidr_block_association import EC2SubnetIpv6CidrBlockAssociation


class EC2DisassociateSubnetCidrBlockResponse(BaseModel):
    Ipv6CidrBlockAssociation: EC2SubnetIpv6CidrBlockAssociation | None = None
    SubnetId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
