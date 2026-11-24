from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_secondary_interface_private_ip_address_specification import EC2SecondaryInterfacePrivateIpAddressSpecification


class EC2LaunchTemplateInstanceSecondaryInterfaceSpecification(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    DeviceIndex: StrictInt | None = None
    PrivateIpAddresses: list[EC2SecondaryInterfacePrivateIpAddressSpecification] | None = None
    PrivateIpAddressCount: StrictInt | None = None
    SecondarySubnetId: StrictStr | None = None
    InterfaceType: StrictStr | None = None
    NetworkCardIndex: StrictInt | None = None
