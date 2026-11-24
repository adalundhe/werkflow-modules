from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_rule_group_rules_details import SecurityHubAwsWafRuleGroupRulesDetails


class SecurityHubAwsWafRuleGroupDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    RuleGroupId: StrictStr | None = None
    Rules: list[SecurityHubAwsWafRuleGroupRulesDetails] | None = None
