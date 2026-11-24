from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_request_policy_config import CloudFrontOriginRequestPolicyConfig


class CloudFrontUpdateOriginRequestPolicyRequest(BaseModel):
    OriginRequestPolicyConfig: CloudFrontOriginRequestPolicyConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
