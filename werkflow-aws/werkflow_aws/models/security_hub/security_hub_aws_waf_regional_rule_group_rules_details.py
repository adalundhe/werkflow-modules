from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_waf_regional_rule_group_rules_action_details import SecurityHubAwsWafRegionalRuleGroupRulesActionDetails


class SecurityHubAwsWafRegionalRuleGroupRulesDetails(BaseModel):
    Action: SecurityHubAwsWafRegionalRuleGroupRulesActionDetails | None = None
    Priority: StrictInt | None = None
    RuleId: StrictStr | None = None
    Type: StrictStr | None = None
