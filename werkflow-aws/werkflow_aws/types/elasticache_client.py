from __future__ import annotations
from abc import ABC, abstractmethod
from botocore.paginate import Paginator
from typing import Any

class ElastiCacheClient(ABC):

    @abstractmethod
    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = True,
        ShowCacheClustersNotInReplicationGroups: bool = True,
    ) -> dict[str, Any]:
        pass
    
    @abstractmethod
    def describe_replication_groups(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(
        self,
        Operation: str,
    ) -> Paginator:
        pass

    @abstractmethod
    def close(self):
        pass