from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_regional_web_acl_rules_list_details import SecurityHubAwsWafRegionalWebAclRulesListDetails


class SecurityHubAwsWafRegionalWebAclDetails(BaseModel):
    DefaultAction: StrictStr | None = None
    MetricName: StrictStr | None = None
    Name: StrictStr | None = None
    RulesList: list[SecurityHubAwsWafRegionalWebAclRulesListDetails] | None = None
    WebAclId: StrictStr | None = None
