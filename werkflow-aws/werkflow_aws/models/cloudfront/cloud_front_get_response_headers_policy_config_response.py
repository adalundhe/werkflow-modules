from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_response_headers_policy_config import CloudFrontResponseHeadersPolicyConfig


class CloudFrontGetResponseHeadersPolicyConfigResponse(BaseModel):
    ResponseHeadersPolicyConfig: CloudFrontResponseHeadersPolicyConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
