from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_vpc_cidr_block_state import EC2VpcCidrBlockState


class EC2VpcIpv6CidrBlockAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    Ipv6CidrBlockState: EC2VpcCidrBlockState | None = None
    NetworkBorderGroup: StrictStr | None = None
    Ipv6Pool: StrictStr | None = None
    Ipv6AddressAttribute: StrictStr | None = None
    IpSource: StrictStr | None = None
