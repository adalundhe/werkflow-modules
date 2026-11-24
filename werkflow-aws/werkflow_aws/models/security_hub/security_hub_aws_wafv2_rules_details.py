from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_wafv2_rules_action_details import SecurityHubAwsWafv2RulesActionDetails
from .security_hub_aws_wafv2_visibility_config_details import SecurityHubAwsWafv2VisibilityConfigDetails


class SecurityHubAwsWafv2RulesDetails(BaseModel):
    Action: SecurityHubAwsWafv2RulesActionDetails | None = None
    Name: StrictStr | None = None
    OverrideAction: StrictStr | None = None
    Priority: StrictInt | None = None
    VisibilityConfig: SecurityHubAwsWafv2VisibilityConfigDetails | None = None
