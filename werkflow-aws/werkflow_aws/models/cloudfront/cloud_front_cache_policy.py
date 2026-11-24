from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_cache_policy_config import CloudFrontCachePolicyConfig


class CloudFrontCachePolicy(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CachePolicyConfig: CloudFrontCachePolicyConfig | None = None
