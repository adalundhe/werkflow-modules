from __future__ import annotations
from abc import ABC, abstractmethod

class ElastiCacheClient(ABC):

    @abstractmethod
    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = True,
        ShowCacheClustersNotInReplicationGroups: bool = True,
    ) -> dict[str, str]:
        pass
        