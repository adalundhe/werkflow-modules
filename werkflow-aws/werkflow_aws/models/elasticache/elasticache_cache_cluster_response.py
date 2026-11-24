from __future__ import annotations
from pydantic import BaseModel
from .elasticache_cache_cluster import ElasticacheCacheCluster


class ElasticacheCacheClusterResponse(BaseModel):
    CacheCluster: ElasticacheCacheCluster | None = None
