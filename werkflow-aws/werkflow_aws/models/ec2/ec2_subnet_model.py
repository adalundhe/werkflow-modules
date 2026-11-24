from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_block_public_access_states import EC2BlockPublicAccessStates
from .ec2_private_dns_name_options_on_launch import EC2PrivateDnsNameOptionsOnLaunch
from .ec2_subnet_ipv6_cidr_block_association import EC2SubnetIpv6CidrBlockAssociation
from .ec2_tag_model import EC2TagModel


class EC2SubnetModel(BaseModel):
    AvailabilityZoneId: StrictStr | None = None
    EnableLniAtDeviceIndex: StrictInt | None = None
    MapCustomerOwnedIpOnLaunch: StrictBool | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    OwnerId: StrictStr | None = None
    AssignIpv6AddressOnCreation: StrictBool | None = None
    Ipv6CidrBlockAssociationSet: list[EC2SubnetIpv6CidrBlockAssociation] | None = None
    Tags: list[EC2TagModel] | None = None
    SubnetArn: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    EnableDns64: StrictBool | None = None
    Ipv6Native: StrictBool | None = None
    PrivateDnsNameOptionsOnLaunch: EC2PrivateDnsNameOptionsOnLaunch | None = None
    BlockPublicAccessStates: EC2BlockPublicAccessStates | None = None
    Type: StrictStr | None = None
    NetworkFirewallConnectivityType: StrictStr | None = None
    SubnetId: StrictStr | None = None
    State: StrictStr | None = None
    VpcId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    AvailableIpAddressCount: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    DefaultForAz: StrictBool | None = None
    MapPublicIpOnLaunch: StrictBool | None = None
