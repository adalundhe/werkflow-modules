from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_wafv2_action_allow_details import SecurityHubAwsWafv2ActionAllowDetails
from .security_hub_aws_wafv2_action_block_details import SecurityHubAwsWafv2ActionBlockDetails
from .security_hub_aws_wafv2_rules_action_captcha_details import SecurityHubAwsWafv2RulesActionCaptchaDetails
from .security_hub_aws_wafv2_rules_action_count_details import SecurityHubAwsWafv2RulesActionCountDetails


class SecurityHubAwsWafv2RulesActionDetails(BaseModel):
    Allow: SecurityHubAwsWafv2ActionAllowDetails | None = None
    Block: SecurityHubAwsWafv2ActionBlockDetails | None = None
    Captcha: SecurityHubAwsWafv2RulesActionCaptchaDetails | None = None
    Count: SecurityHubAwsWafv2RulesActionCountDetails | None = None
