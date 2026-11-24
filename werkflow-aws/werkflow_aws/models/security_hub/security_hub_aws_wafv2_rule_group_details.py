from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_wafv2_rules_details import SecurityHubAwsWafv2RulesDetails
from .security_hub_aws_wafv2_visibility_config_details import SecurityHubAwsWafv2VisibilityConfigDetails


class SecurityHubAwsWafv2RuleGroupDetails(BaseModel):
    Capacity: StrictInt | None = None
    Description: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Rules: list[SecurityHubAwsWafv2RulesDetails] | None = None
    Scope: StrictStr | None = None
    VisibilityConfig: SecurityHubAwsWafv2VisibilityConfigDetails | None = None
