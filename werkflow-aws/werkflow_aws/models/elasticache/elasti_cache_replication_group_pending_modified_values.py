from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_pending_log_delivery_configuration import ElastiCachePendingLogDeliveryConfiguration
from .elasti_cache_resharding_status import ElastiCacheReshardingStatus
from .elasti_cache_user_groups_update_status import ElastiCacheUserGroupsUpdateStatus


class ElastiCacheReplicationGroupPendingModifiedValues(BaseModel):
    PrimaryClusterId: StrictStr | None = None
    AutomaticFailoverStatus: StrictStr | None = None
    Resharding: ElastiCacheReshardingStatus | None = None
    AuthTokenStatus: StrictStr | None = None
    UserGroups: ElastiCacheUserGroupsUpdateStatus | None = None
    LogDeliveryConfigurations: list[ElastiCachePendingLogDeliveryConfiguration] | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    TransitEncryptionMode: StrictStr | None = None
    ClusterMode: StrictStr | None = None
