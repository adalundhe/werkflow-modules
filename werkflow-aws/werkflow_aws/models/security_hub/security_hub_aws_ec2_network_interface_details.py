from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_ec2_network_interface_attachment import SecurityHubAwsEc2NetworkInterfaceAttachment
from .security_hub_aws_ec2_network_interface_ip_v6_address_detail import SecurityHubAwsEc2NetworkInterfaceIpV6AddressDetail
from .security_hub_aws_ec2_network_interface_private_ip_address_detail import SecurityHubAwsEc2NetworkInterfacePrivateIpAddressDetail
from .security_hub_aws_ec2_network_interface_security_group import SecurityHubAwsEc2NetworkInterfaceSecurityGroup


class SecurityHubAwsEc2NetworkInterfaceDetails(BaseModel):
    Attachment: SecurityHubAwsEc2NetworkInterfaceAttachment | None = None
    NetworkInterfaceId: StrictStr | None = None
    SecurityGroups: list[SecurityHubAwsEc2NetworkInterfaceSecurityGroup] | None = None
    SourceDestCheck: StrictBool | None = None
    IpV6Addresses: list[SecurityHubAwsEc2NetworkInterfaceIpV6AddressDetail] | None = None
    PrivateIpAddresses: list[SecurityHubAwsEc2NetworkInterfacePrivateIpAddressDetail] | None = None
    PublicDnsName: StrictStr | None = None
    PublicIp: StrictStr | None = None
