from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_firewall_policy_stateful_rule_group_references_details import SecurityHubFirewallPolicyStatefulRuleGroupReferencesDetails
from .security_hub_firewall_policy_stateless_custom_actions_details import SecurityHubFirewallPolicyStatelessCustomActionsDetails
from .security_hub_firewall_policy_stateless_rule_group_references_details import SecurityHubFirewallPolicyStatelessRuleGroupReferencesDetails


class SecurityHubFirewallPolicyDetails(BaseModel):
    StatefulRuleGroupReferences: list[SecurityHubFirewallPolicyStatefulRuleGroupReferencesDetails] | None = None
    StatelessCustomActions: list[SecurityHubFirewallPolicyStatelessCustomActionsDetails] | None = None
    StatelessDefaultActions: list[StrictStr] | None = None
    StatelessFragmentDefaultActions: list[StrictStr] | None = None
    StatelessRuleGroupReferences: list[SecurityHubFirewallPolicyStatelessRuleGroupReferencesDetails] | None = None
