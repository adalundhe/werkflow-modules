from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_time_range_filter import ElastiCacheTimeRangeFilter


class ElastiCacheDescribeUpdateActionsRequest(BaseModel):
    ServiceUpdateName: StrictStr | None = None
    ReplicationGroupIds: list[StrictStr] | None = None
    CacheClusterIds: list[StrictStr] | None = None
    Engine: StrictStr | None = None
    ServiceUpdateStatus: list[Literal['available', 'cancelled', 'expired']] | None = None
    ServiceUpdateTimeRange: ElastiCacheTimeRangeFilter | None = None
    UpdateActionStatus: list[Literal['not-applied', 'waiting-to-start', 'in-progress', 'stopping', 'stopped', 'complete', 'scheduling', 'scheduled', 'not-applicable']] | None = None
    ShowNodeLevelUpdateStatus: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
