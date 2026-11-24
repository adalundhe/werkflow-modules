from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_response_headers_policy_config import CloudFrontResponseHeadersPolicyConfig


class CloudFrontUpdateResponseHeadersPolicyRequest(BaseModel):
    ResponseHeadersPolicyConfig: CloudFrontResponseHeadersPolicyConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
