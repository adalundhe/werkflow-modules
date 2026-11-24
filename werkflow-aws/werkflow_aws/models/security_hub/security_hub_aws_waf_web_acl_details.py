from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_waf_web_acl_rule import SecurityHubAwsWafWebAclRule


class SecurityHubAwsWafWebAclDetails(BaseModel):
    Name: StrictStr | None = None
    DefaultAction: StrictStr | None = None
    Rules: list[SecurityHubAwsWafWebAclRule] | None = None
    WebAclId: StrictStr | None = None
