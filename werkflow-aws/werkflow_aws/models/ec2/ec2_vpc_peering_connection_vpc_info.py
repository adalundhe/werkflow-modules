from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_cidr_block import EC2CidrBlock
from .ec2_ipv6_cidr_block import EC2Ipv6CidrBlock
from .ec2_vpc_peering_connection_options_description import EC2VpcPeeringConnectionOptionsDescription


class EC2VpcPeeringConnectionVpcInfo(BaseModel):
    CidrBlock: StrictStr | None = None
    Ipv6CidrBlockSet: list[EC2Ipv6CidrBlock] | None = None
    CidrBlockSet: list[EC2CidrBlock] | None = None
    OwnerId: StrictStr | None = None
    PeeringOptions: EC2VpcPeeringConnectionOptionsDescription | None = None
    VpcId: StrictStr | None = None
    Region: StrictStr | None = None
