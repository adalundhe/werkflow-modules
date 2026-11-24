from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_wafv2_custom_http_header import SecurityHubAwsWafv2CustomHttpHeader


class SecurityHubAwsWafv2CustomRequestHandlingDetails(BaseModel):
    InsertHeaders: list[SecurityHubAwsWafv2CustomHttpHeader] | None = None
