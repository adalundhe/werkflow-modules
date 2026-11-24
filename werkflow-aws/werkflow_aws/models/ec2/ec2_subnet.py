from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag import EC2Tag


class EC2Subnet(BaseModel):
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AvailableIpAddressCount: StrictInt | None = None
    CidrBlock: StrictStr | None = None
    DefaultForAz: StrictBool | None = None
    MapPublicIpOnLaunch: StrictBool | None = None
    State: StrictStr | None = None
    OwnerId: StrictStr | None = None
    SubnetArn: StrictStr | None = None
    Tags: list[EC2Tag] | None = None
