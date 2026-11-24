from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_elb_app_cookie_stickiness_policy import SecurityHubAwsElbAppCookieStickinessPolicy
from .security_hub_aws_elb_lb_cookie_stickiness_policy import SecurityHubAwsElbLbCookieStickinessPolicy


class SecurityHubAwsElbLoadBalancerPolicies(BaseModel):
    AppCookieStickinessPolicies: list[SecurityHubAwsElbAppCookieStickinessPolicy] | None = None
    LbCookieStickinessPolicies: list[SecurityHubAwsElbLbCookieStickinessPolicy] | None = None
    OtherPolicies: list[StrictStr] | None = None
