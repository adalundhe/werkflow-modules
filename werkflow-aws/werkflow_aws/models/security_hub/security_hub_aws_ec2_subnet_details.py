from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_ipv6_cidr_block_association import SecurityHubIpv6CidrBlockAssociation


class SecurityHubAwsEc2SubnetDetails(BaseModel):
    AssignIpv6AddressOnCreation: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AvailableIpAddressCount: StrictInt | None = None
    CidrBlock: StrictStr | None = None
    DefaultForAz: StrictBool | None = None
    MapPublicIpOnLaunch: StrictBool | None = None
    OwnerId: StrictStr | None = None
    State: StrictStr | None = None
    SubnetArn: StrictStr | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    Ipv6CidrBlockAssociationSet: list[SecurityHubIpv6CidrBlockAssociation] | None = None
