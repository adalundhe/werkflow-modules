from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_network_firewall_policy_description import FMSNetworkFirewallPolicyDescription


class FMSNetworkFirewallPolicyModifiedViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    CurrentPolicyDescription: FMSNetworkFirewallPolicyDescription | None = None
    ExpectedPolicyDescription: FMSNetworkFirewallPolicyDescription | None = None
