from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_waf_action import SecurityHubWafAction
from .security_hub_waf_excluded_rule import SecurityHubWafExcludedRule
from .security_hub_waf_override_action import SecurityHubWafOverrideAction


class SecurityHubAwsWafWebAclRule(BaseModel):
    Action: SecurityHubWafAction | None = None
    ExcludedRules: list[SecurityHubWafExcludedRule] | None = None
    OverrideAction: SecurityHubWafOverrideAction | None = None
    Priority: StrictInt | None = None
    RuleId: StrictStr | None = None
    Type: StrictStr | None = None
