from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_subnet_cidr_block_state import EC2SubnetCidrBlockState


class EC2SubnetIpv6CidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    Ipv6CidrBlockState: EC2SubnetCidrBlockState | None = None
    Ipv6AddressAttribute: StrictStr | None = None
    IpSource: StrictStr | None = None
