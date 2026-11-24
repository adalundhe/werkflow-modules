from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_request_policy_config import CloudFrontOriginRequestPolicyConfig


class CloudFrontGetOriginRequestPolicyConfigResponse(BaseModel):
    OriginRequestPolicyConfig: CloudFrontOriginRequestPolicyConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
