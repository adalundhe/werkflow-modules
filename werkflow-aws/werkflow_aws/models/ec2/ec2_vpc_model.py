from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_block_public_access_states import EC2BlockPublicAccessStates
from .ec2_network_firewall_association import EC2NetworkFirewallAssociation
from .ec2_tag_model import EC2TagModel
from .ec2_vpc_cidr_block_association import EC2VpcCidrBlockAssociation
from .ec2_vpc_encryption_control import EC2VpcEncryptionControl
from .ec2_vpc_ipv6_cidr_block_association import EC2VpcIpv6CidrBlockAssociation


class EC2VpcModel(BaseModel):
    OwnerId: StrictStr | None = None
    InstanceTenancy: StrictStr | None = None
    Ipv6CidrBlockAssociationSet: list[EC2VpcIpv6CidrBlockAssociation] | None = None
    CidrBlockAssociationSet: list[EC2VpcCidrBlockAssociation] | None = None
    IsDefault: StrictBool | None = None
    EncryptionControl: EC2VpcEncryptionControl | None = None
    Tags: list[EC2TagModel] | None = None
    BlockPublicAccessStates: EC2BlockPublicAccessStates | None = None
    NetworkFirewallAssociations: list[EC2NetworkFirewallAssociation] | None = None
    VpcId: StrictStr | None = None
    State: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    DhcpOptionsId: StrictStr | None = None
