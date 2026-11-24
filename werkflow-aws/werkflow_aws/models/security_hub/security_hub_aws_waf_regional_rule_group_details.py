from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_regional_rule_group_rules_details import SecurityHubAwsWafRegionalRuleGroupRulesDetails


class SecurityHubAwsWafRegionalRuleGroupDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    RuleGroupId: StrictStr | None = None
    Rules: list[SecurityHubAwsWafRegionalRuleGroupRulesDetails] | None = None
