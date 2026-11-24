from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_firewall_policy_details import SecurityHubFirewallPolicyDetails


class SecurityHubAwsNetworkFirewallFirewallPolicyDetails(BaseModel):
    FirewallPolicy: SecurityHubFirewallPolicyDetails | None = None
    FirewallPolicyArn: StrictStr | None = None
    FirewallPolicyId: StrictStr | None = None
    FirewallPolicyName: StrictStr | None = None
    Description: StrictStr | None = None
