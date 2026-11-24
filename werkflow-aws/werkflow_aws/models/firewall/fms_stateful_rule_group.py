from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .fms_network_firewall_stateful_rule_group_override import FMSNetworkFirewallStatefulRuleGroupOverride


class FMSStatefulRuleGroup(BaseModel):
    RuleGroupName: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Priority: StrictInt | None = None
    Override: FMSNetworkFirewallStatefulRuleGroupOverride | None = None
