from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_details import SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails
from .security_hub_aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_details import SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails
from .security_hub_aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_details import SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails
from .security_hub_aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_details import SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails


class SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetDetails(BaseModel):
    AssociateCarrierIpAddress: StrictBool | None = None
    AssociatePublicIpAddress: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Description: StrictStr | None = None
    DeviceIndex: StrictInt | None = None
    Groups: list[StrictStr] | None = None
    InterfaceType: StrictStr | None = None
    Ipv4PrefixCount: StrictInt | None = None
    Ipv4Prefixes: list[SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails] | None = None
    Ipv6AddressCount: StrictInt | None = None
    Ipv6Addresses: list[SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails] | None = None
    Ipv6PrefixCount: StrictInt | None = None
    Ipv6Prefixes: list[SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails] | None = None
    NetworkCardIndex: StrictInt | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PrivateIpAddresses: list[SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
    SubnetId: StrictStr | None = None
