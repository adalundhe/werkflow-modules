from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_endpoint import ElastiCacheEndpoint


class ElastiCacheNodeGroupMember(BaseModel):
    CacheClusterId: StrictStr | None = None
    CacheNodeId: StrictStr | None = None
    ReadEndpoint: ElastiCacheEndpoint | None = None
    PreferredAvailabilityZone: StrictStr | None = None
    PreferredOutpostArn: StrictStr | None = None
    CurrentRole: StrictStr | None = None
