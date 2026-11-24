from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_waf_rule_group_rules_action_details import SecurityHubAwsWafRuleGroupRulesActionDetails


class SecurityHubAwsWafRuleGroupRulesDetails(BaseModel):
    Action: SecurityHubAwsWafRuleGroupRulesActionDetails | None = None
    Priority: StrictInt | None = None
    RuleId: StrictStr | None = None
    Type: StrictStr | None = None
