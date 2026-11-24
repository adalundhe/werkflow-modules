from __future__ import annotations
from pydantic import BaseModel
from .fms_network_acl_common_policy import FMSNetworkAclCommonPolicy
from .fms_network_firewall_policy import FMSNetworkFirewallPolicy
from .fms_third_party_firewall_policy import FMSThirdPartyFirewallPolicy


class FMSPolicyOption(BaseModel):
    NetworkFirewallPolicy: FMSNetworkFirewallPolicy | None = None
    ThirdPartyFirewallPolicy: FMSThirdPartyFirewallPolicy | None = None
    NetworkAclCommonPolicy: FMSNetworkAclCommonPolicy | None = None
