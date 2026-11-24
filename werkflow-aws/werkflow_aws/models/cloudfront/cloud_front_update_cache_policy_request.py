from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_cache_policy_config import CloudFrontCachePolicyConfig


class CloudFrontUpdateCachePolicyRequest(BaseModel):
    CachePolicyConfig: CloudFrontCachePolicyConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
