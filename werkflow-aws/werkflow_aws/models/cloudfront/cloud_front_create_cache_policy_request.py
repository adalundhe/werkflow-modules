from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_cache_policy_config import CloudFrontCachePolicyConfig


class CloudFrontCreateCachePolicyRequest(BaseModel):
    CachePolicyConfig: CloudFrontCachePolicyConfig
