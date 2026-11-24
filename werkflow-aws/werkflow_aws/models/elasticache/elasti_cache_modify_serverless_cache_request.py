from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_cache_usage_limits import ElastiCacheCacheUsageLimits


class ElastiCacheModifyServerlessCacheRequest(BaseModel):
    ServerlessCacheName: StrictStr
    Description: StrictStr | None = None
    CacheUsageLimits: ElastiCacheCacheUsageLimits | None = None
    RemoveUserGroup: StrictBool | None = None
    UserGroupId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    DailySnapshotTime: StrictStr | None = None
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
