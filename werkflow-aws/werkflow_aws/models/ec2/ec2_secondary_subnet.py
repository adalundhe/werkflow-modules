from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_secondary_subnet_ipv4_cidr_block_association import EC2SecondarySubnetIpv4CidrBlockAssociation
from .ec2_tag_model import EC2TagModel


class EC2SecondarySubnet(BaseModel):
    SecondarySubnetId: StrictStr | None = None
    SecondarySubnetArn: StrictStr | None = None
    SecondaryNetworkId: StrictStr | None = None
    SecondaryNetworkType: StrictStr | None = None
    OwnerId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Ipv4CidrBlockAssociations: list[EC2SecondarySubnetIpv4CidrBlockAssociation] | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
