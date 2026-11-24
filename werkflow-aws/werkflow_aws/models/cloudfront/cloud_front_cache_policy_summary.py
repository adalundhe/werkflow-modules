from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_cache_policy import CloudFrontCachePolicy


class CloudFrontCachePolicySummary(BaseModel):
    Type: StrictStr | None = None
    CachePolicy: CloudFrontCachePolicy | None = None
