from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_scheduled_instances_ipv6_address import EC2ScheduledInstancesIpv6Address
from .ec2_scheduled_instances_private_ip_address_config import EC2ScheduledInstancesPrivateIpAddressConfig


class EC2ScheduledInstancesNetworkInterface(BaseModel):
    AssociatePublicIpAddress: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Description: StrictStr | None = None
    DeviceIndex: StrictInt | None = None
    Groups: list[StrictStr] | None = None
    Ipv6AddressCount: StrictInt | None = None
    Ipv6Addresses: list[EC2ScheduledInstancesIpv6Address] | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PrivateIpAddressConfigs: list[EC2ScheduledInstancesPrivateIpAddressConfig] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
    SubnetId: StrictStr | None = None
