from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_connection_tracking_specification_request import EC2ConnectionTrackingSpecificationRequest
from .ec2_instance_ipv6_address import EC2InstanceIpv6Address
from .ec2_ipv4_prefix_specification_request import EC2Ipv4PrefixSpecificationRequest
from .ec2_ipv6_prefix_specification_request import EC2Ipv6PrefixSpecificationRequest
from .ec2_operator_request import EC2OperatorRequest
from .ec2_private_ip_address_specification import EC2PrivateIpAddressSpecification
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateNetworkInterfaceRequest(BaseModel):
    SubnetId: StrictStr
    Ipv4Prefixes: list[EC2Ipv4PrefixSpecificationRequest] | None = None
    Ipv4PrefixCount: StrictInt | None = None
    Ipv6Prefixes: list[EC2Ipv6PrefixSpecificationRequest] | None = None
    Ipv6PrefixCount: StrictInt | None = None
    InterfaceType: Literal['efa', 'efa-only', 'branch', 'trunk'] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    EnablePrimaryIpv6: StrictBool | None = None
    ConnectionTrackingSpecification: EC2ConnectionTrackingSpecificationRequest | None = None
    Operator: EC2OperatorRequest | None = None
    Description: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    Groups: list[StrictStr] | None = None
    PrivateIpAddresses: list[EC2PrivateIpAddressSpecification] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
    Ipv6Addresses: list[EC2InstanceIpv6Address] | None = None
    Ipv6AddressCount: StrictInt | None = None
    DryRun: StrictBool | None = None
