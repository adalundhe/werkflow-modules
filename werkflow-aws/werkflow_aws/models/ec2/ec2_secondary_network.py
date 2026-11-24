from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_secondary_network_ipv4_cidr_block_association import EC2SecondaryNetworkIpv4CidrBlockAssociation
from .ec2_tag_model import EC2TagModel


class EC2SecondaryNetwork(BaseModel):
    SecondaryNetworkId: StrictStr | None = None
    SecondaryNetworkArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    Ipv4CidrBlockAssociations: list[EC2SecondaryNetworkIpv4CidrBlockAssociation] | None = None
    Tags: list[EC2TagModel] | None = None
