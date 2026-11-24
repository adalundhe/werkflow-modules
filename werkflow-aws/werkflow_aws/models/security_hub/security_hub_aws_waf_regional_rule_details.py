from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_regional_rule_predicate_list_details import SecurityHubAwsWafRegionalRulePredicateListDetails


class SecurityHubAwsWafRegionalRuleDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    PredicateList: list[SecurityHubAwsWafRegionalRulePredicateListDetails] | None = None
    RuleId: StrictStr | None = None
