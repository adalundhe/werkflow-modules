from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_network_firewall_firewall_subnet_mappings_details import SecurityHubAwsNetworkFirewallFirewallSubnetMappingsDetails


class SecurityHubAwsNetworkFirewallFirewallDetails(BaseModel):
    DeleteProtection: StrictBool | None = None
    Description: StrictStr | None = None
    FirewallArn: StrictStr | None = None
    FirewallId: StrictStr | None = None
    FirewallName: StrictStr | None = None
    FirewallPolicyArn: StrictStr | None = None
    FirewallPolicyChangeProtection: StrictBool | None = None
    SubnetChangeProtection: StrictBool | None = None
    SubnetMappings: list[SecurityHubAwsNetworkFirewallFirewallSubnetMappingsDetails] | None = None
    VpcId: StrictStr | None = None
