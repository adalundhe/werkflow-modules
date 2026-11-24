from pydantic import BaseModel, StrictStr
from .elasticache_cache_cluster import ElasticacheCacheCluster


class ElasticacheDescribeCacheClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    CacheClusters: list[ElasticacheCacheCluster] | None = None
