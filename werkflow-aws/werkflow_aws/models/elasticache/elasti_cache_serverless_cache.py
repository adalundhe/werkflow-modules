from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .elasti_cache_cache_usage_limits import ElastiCacheCacheUsageLimits
from .elasti_cache_endpoint import ElastiCacheEndpoint
from .elasti_cache_integration import ElastiCacheIntegration
from .elasti_cache_migration_summary import ElastiCacheMigrationSummary


class ElastiCacheServerlessCache(BaseModel):
    ServerlessCacheName: StrictStr | None = None
    Description: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    FullEngineVersion: StrictStr | None = None
    CacheUsageLimits: ElastiCacheCacheUsageLimits | None = None
    KmsKeyId: StrictStr | None = None
    StorageEncryptionType: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Endpoint: ElastiCacheEndpoint | None = None
    ReaderEndpoint: ElastiCacheEndpoint | None = None
    ARN: StrictStr | None = None
    UserGroupId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    DailySnapshotTime: StrictStr | None = None
    NetworkType: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    Migration: ElastiCacheMigrationSummary | None = None
    Integrations: list[ElastiCacheIntegration] | None = None
