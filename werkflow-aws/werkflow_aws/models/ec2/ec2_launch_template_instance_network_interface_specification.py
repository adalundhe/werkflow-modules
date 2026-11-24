from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_connection_tracking_specification import EC2ConnectionTrackingSpecification
from .ec2_instance_ipv6_address import EC2InstanceIpv6Address
from .ec2_ipv4_prefix_specification_response import EC2Ipv4PrefixSpecificationResponse
from .ec2_ipv6_prefix_specification_response import EC2Ipv6PrefixSpecificationResponse
from .ec2_launch_template_ena_srd_specification import EC2LaunchTemplateEnaSrdSpecification
from .ec2_private_ip_address_specification import EC2PrivateIpAddressSpecification


class EC2LaunchTemplateInstanceNetworkInterfaceSpecification(BaseModel):
    AssociateCarrierIpAddress: StrictBool | None = None
    AssociatePublicIpAddress: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Description: StrictStr | None = None
    DeviceIndex: StrictInt | None = None
    Groups: list[StrictStr] | None = None
    InterfaceType: StrictStr | None = None
    Ipv6AddressCount: StrictInt | None = None
    Ipv6Addresses: list[EC2InstanceIpv6Address] | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PrivateIpAddresses: list[EC2PrivateIpAddressSpecification] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
    SubnetId: StrictStr | None = None
    NetworkCardIndex: StrictInt | None = None
    Ipv4Prefixes: list[EC2Ipv4PrefixSpecificationResponse] | None = None
    Ipv4PrefixCount: StrictInt | None = None
    Ipv6Prefixes: list[EC2Ipv6PrefixSpecificationResponse] | None = None
    Ipv6PrefixCount: StrictInt | None = None
    PrimaryIpv6: StrictBool | None = None
    EnaSrdSpecification: EC2LaunchTemplateEnaSrdSpecification | None = None
    ConnectionTrackingSpecification: EC2ConnectionTrackingSpecification | None = None
    EnaQueueCount: StrictInt | None = None
