from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_wafv2_custom_http_header import SecurityHubAwsWafv2CustomHttpHeader


class SecurityHubAwsWafv2CustomResponseDetails(BaseModel):
    CustomResponseBodyKey: StrictStr | None = None
    ResponseCode: StrictInt | None = None
    ResponseHeaders: list[SecurityHubAwsWafv2CustomHttpHeader] | None = None
