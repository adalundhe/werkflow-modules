from pydantic import BaseModel, StrictStr
from .cache_cluster import CacheCluster


class DescribeCacheClustersResponse(BaseModel):
    Marker: StrictStr
    CacheClusters: list[CacheCluster]

