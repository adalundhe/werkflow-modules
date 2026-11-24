from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .elasti_cache_node_group_configuration import ElastiCacheNodeGroupConfiguration


class ElastiCacheNodeSnapshot(BaseModel):
    CacheClusterId: StrictStr | None = None
    NodeGroupId: StrictStr | None = None
    CacheNodeId: StrictStr | None = None
    NodeGroupConfiguration: ElastiCacheNodeGroupConfiguration | None = None
    CacheSize: StrictStr | None = None
    CacheNodeCreateTime: datetime.datetime | StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | StrictStr | None = None
