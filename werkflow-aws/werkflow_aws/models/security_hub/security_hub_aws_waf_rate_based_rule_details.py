from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_waf_rate_based_rule_match_predicate import SecurityHubAwsWafRateBasedRuleMatchPredicate


class SecurityHubAwsWafRateBasedRuleDetails(BaseModel):
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    RateKey: StrictStr | None = None
    RateLimit: StrictInt | None = None
    RuleId: StrictStr | None = None
    MatchPredicates: list[SecurityHubAwsWafRateBasedRuleMatchPredicate] | None = None
