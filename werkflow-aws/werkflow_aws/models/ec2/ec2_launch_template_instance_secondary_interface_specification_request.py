from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_secondary_interface_private_ip_address_specification_request import EC2SecondaryInterfacePrivateIpAddressSpecificationRequest


class EC2LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    DeviceIndex: StrictInt | None = None
    PrivateIpAddresses: list[EC2SecondaryInterfacePrivateIpAddressSpecificationRequest] | None = None
    PrivateIpAddressCount: StrictInt | None = None
    SecondarySubnetId: StrictStr | None = None
    InterfaceType: Literal['secondary'] | None = None
    NetworkCardIndex: StrictInt | None = None
