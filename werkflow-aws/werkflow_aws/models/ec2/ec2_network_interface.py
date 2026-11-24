from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_connection_tracking_configuration import EC2ConnectionTrackingConfiguration
from .ec2_group_identifier_model import EC2GroupIdentifierModel
from .ec2_ipv4_prefix_specification import EC2Ipv4PrefixSpecification
from .ec2_ipv6_prefix_specification import EC2Ipv6PrefixSpecification
from .ec2_network_interface_association import EC2NetworkInterfaceAssociation
from .ec2_network_interface_attachment import EC2NetworkInterfaceAttachment
from .ec2_network_interface_ipv6_address import EC2NetworkInterfaceIpv6Address
from .ec2_network_interface_private_ip_address import EC2NetworkInterfacePrivateIpAddress
from .ec2_operator_response import EC2OperatorResponse
from .ec2_public_ip_dns_name_options import EC2PublicIpDnsNameOptions
from .ec2_tag_model import EC2TagModel


class EC2NetworkInterface(BaseModel):
    Association: EC2NetworkInterfaceAssociation | None = None
    Attachment: EC2NetworkInterfaceAttachment | None = None
    AvailabilityZone: StrictStr | None = None
    ConnectionTrackingConfiguration: EC2ConnectionTrackingConfiguration | None = None
    Description: StrictStr | None = None
    Groups: list[EC2GroupIdentifierModel] | None = None
    InterfaceType: StrictStr | None = None
    Ipv6Addresses: list[EC2NetworkInterfaceIpv6Address] | None = None
    MacAddress: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    PrivateDnsName: StrictStr | None = None
    PublicDnsName: StrictStr | None = None
    PublicIpDnsNameOptions: EC2PublicIpDnsNameOptions | None = None
    PrivateIpAddress: StrictStr | None = None
    PrivateIpAddresses: list[EC2NetworkInterfacePrivateIpAddress] | None = None
    Ipv4Prefixes: list[EC2Ipv4PrefixSpecification] | None = None
    Ipv6Prefixes: list[EC2Ipv6PrefixSpecification] | None = None
    RequesterId: StrictStr | None = None
    RequesterManaged: StrictBool | None = None
    SourceDestCheck: StrictBool | None = None
    Status: StrictStr | None = None
    SubnetId: StrictStr | None = None
    TagSet: list[EC2TagModel] | None = None
    VpcId: StrictStr | None = None
    DenyAllIgwTraffic: StrictBool | None = None
    Ipv6Native: StrictBool | None = None
    Ipv6Address: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    AssociatedSubnets: list[StrictStr] | None = None
    AvailabilityZoneId: StrictStr | None = None
