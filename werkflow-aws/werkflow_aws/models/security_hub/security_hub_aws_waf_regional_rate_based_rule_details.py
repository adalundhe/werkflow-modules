from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_waf_regional_rate_based_rule_match_predicate import SecurityHubAwsWafRegionalRateBasedRuleMatchPredicate


class SecurityHubAwsWafRegionalRateBasedRuleDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    RateKey: StrictStr | None = None
    RateLimit: StrictInt | None = None
    RuleId: StrictStr | None = None
    MatchPredicates: list[SecurityHubAwsWafRegionalRateBasedRuleMatchPredicate] | None = None
