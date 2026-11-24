from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_availability_zone_address import EC2AvailabilityZoneAddress
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateNatGatewayRequest(BaseModel):
    AvailabilityMode: Literal['zonal', 'regional'] | None = None
    AllocationId: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    AvailabilityZoneAddresses: list[EC2AvailabilityZoneAddress] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ConnectivityType: Literal['private', 'public'] | None = None
    PrivateIpAddress: StrictStr | None = None
    SecondaryAllocationIds: list[StrictStr] | None = None
    SecondaryPrivateIpAddresses: list[StrictStr] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
