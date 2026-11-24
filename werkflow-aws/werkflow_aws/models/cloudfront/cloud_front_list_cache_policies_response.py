from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_cache_policy_list import CloudFrontCachePolicyList


class CloudFrontListCachePoliciesResponse(BaseModel):
    CachePolicyList: CloudFrontCachePolicyList | None = None
    ResponseMetadata: dict[str, Any] | None = None
