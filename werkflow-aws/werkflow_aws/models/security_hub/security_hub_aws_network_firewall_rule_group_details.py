from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_rule_group_details import SecurityHubRuleGroupDetails


class SecurityHubAwsNetworkFirewallRuleGroupDetails(BaseModel):
    Capacity: StrictInt | None = None
    Description: StrictStr | None = None
    RuleGroup: SecurityHubRuleGroupDetails | None = None
    RuleGroupArn: StrictStr | None = None
    RuleGroupId: StrictStr | None = None
    RuleGroupName: StrictStr | None = None
    Type: StrictStr | None = None
