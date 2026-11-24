from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_node_update_status import ElastiCacheCacheNodeUpdateStatus
from .elasti_cache_node_group_update_status import ElastiCacheNodeGroupUpdateStatus


class ElastiCacheUpdateAction(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    ServiceUpdateName: StrictStr | None = None
    ServiceUpdateReleaseDate: datetime.datetime | StrictStr | None = None
    ServiceUpdateSeverity: StrictStr | None = None
    ServiceUpdateStatus: StrictStr | None = None
    ServiceUpdateRecommendedApplyByDate: datetime.datetime | StrictStr | None = None
    ServiceUpdateType: StrictStr | None = None
    UpdateActionAvailableDate: datetime.datetime | StrictStr | None = None
    UpdateActionStatus: StrictStr | None = None
    NodesUpdated: StrictStr | None = None
    UpdateActionStatusModifiedDate: datetime.datetime | StrictStr | None = None
    SlaMet: StrictStr | None = None
    NodeGroupUpdateStatus: list[ElastiCacheNodeGroupUpdateStatus] | None = None
    CacheNodeUpdateStatus: list[ElastiCacheCacheNodeUpdateStatus] | None = None
    EstimatedUpdateTime: StrictStr | None = None
    Engine: StrictStr | None = None
