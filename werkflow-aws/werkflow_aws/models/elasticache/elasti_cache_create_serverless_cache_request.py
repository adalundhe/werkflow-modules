from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .elasti_cache_cache_usage_limits import ElastiCacheCacheUsageLimits
from .elasti_cache_integration_request import ElastiCacheIntegrationRequest
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateServerlessCacheRequest(BaseModel):
    ServerlessCacheName: StrictStr
    Engine: StrictStr
    Description: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    CacheUsageLimits: ElastiCacheCacheUsageLimits | None = None
    KmsKeyId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SnapshotArnsToRestore: list[StrictStr] | None = None
    Tags: list[ElastiCacheTag] | None = None
    UserGroupId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    DailySnapshotTime: StrictStr | None = None
    NetworkType: Literal['ipv4', 'ipv6', 'dual_stack'] | None = None
    ConnectionType: Literal['vpc', 'public'] | None = None
    Integrations: list[ElastiCacheIntegrationRequest] | None = None
