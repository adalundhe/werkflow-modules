from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_cache_policy import CloudFrontCachePolicy


class CloudFrontUpdateCachePolicyResponse(BaseModel):
    CachePolicy: CloudFrontCachePolicy | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
