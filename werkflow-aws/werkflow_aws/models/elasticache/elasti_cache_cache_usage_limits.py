from __future__ import annotations
from pydantic import BaseModel
from .elasti_cache_data_storage import ElastiCacheDataStorage
from .elasti_cache_ecpu_per_second import ElastiCacheECPUPerSecond


class ElastiCacheCacheUsageLimits(BaseModel):
    DataStorage: ElastiCacheDataStorage | None = None
    ECPUPerSecond: ElastiCacheECPUPerSecond | None = None
