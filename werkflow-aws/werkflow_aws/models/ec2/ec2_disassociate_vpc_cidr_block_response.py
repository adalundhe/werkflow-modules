from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_cidr_block_association import EC2VpcCidrBlockAssociation
from .ec2_vpc_ipv6_cidr_block_association import EC2VpcIpv6CidrBlockAssociation


class EC2DisassociateVpcCidrBlockResponse(BaseModel):
    Ipv6CidrBlockAssociation: EC2VpcIpv6CidrBlockAssociation | None = None
    CidrBlockAssociation: EC2VpcCidrBlockAssociation | None = None
    VpcId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
