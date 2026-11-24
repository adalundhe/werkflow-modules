from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_rule_predicate_list_details import SecurityHubAwsWafRulePredicateListDetails


class SecurityHubAwsWafRuleDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    PredicateList: list[SecurityHubAwsWafRulePredicateListDetails] | None = None
    RuleId: StrictStr | None = None
