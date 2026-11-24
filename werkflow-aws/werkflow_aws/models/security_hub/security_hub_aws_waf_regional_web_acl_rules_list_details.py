from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_waf_regional_web_acl_rules_list_action_details import SecurityHubAwsWafRegionalWebAclRulesListActionDetails
from .security_hub_aws_waf_regional_web_acl_rules_list_override_action_details import SecurityHubAwsWafRegionalWebAclRulesListOverrideActionDetails


class SecurityHubAwsWafRegionalWebAclRulesListDetails(BaseModel):
    Action: SecurityHubAwsWafRegionalWebAclRulesListActionDetails | None = None
    OverrideAction: SecurityHubAwsWafRegionalWebAclRulesListOverrideActionDetails | None = None
    Priority: StrictInt | None = None
    RuleId: StrictStr | None = None
    Type: StrictStr | None = None
