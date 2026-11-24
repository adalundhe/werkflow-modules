from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_wafv2_rules_details import SecurityHubAwsWafv2RulesDetails
from .security_hub_aws_wafv2_visibility_config_details import SecurityHubAwsWafv2VisibilityConfigDetails
from .security_hub_aws_wafv2_web_acl_action_details import SecurityHubAwsWafv2WebAclActionDetails
from .security_hub_aws_wafv2_web_acl_captcha_config_details import SecurityHubAwsWafv2WebAclCaptchaConfigDetails


class SecurityHubAwsWafv2WebAclDetails(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    ManagedbyFirewallManager: StrictBool | None = None
    Id: StrictStr | None = None
    Capacity: StrictInt | None = None
    CaptchaConfig: SecurityHubAwsWafv2WebAclCaptchaConfigDetails | None = None
    DefaultAction: SecurityHubAwsWafv2WebAclActionDetails | None = None
    Description: StrictStr | None = None
    Rules: list[SecurityHubAwsWafv2RulesDetails] | None = None
    VisibilityConfig: SecurityHubAwsWafv2VisibilityConfigDetails | None = None
