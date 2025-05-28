from pydantic import BaseModel, StrictStr
from .elasticache_global_replication_group_info import ElasticacheGlobalReplicationGroupInfo
from .elasticache_pending_modified_values import ElasticachePendingModifiedValues

class ElasticacheReplicationGroup(BaseModel):
    ReplicationGroupId: StrictStr
    Description: StrictStr
    GlobalReplicationGroupInfo: ElasticacheGlobalReplicationGroupInfo
    Status: StrictStr
    PendingModifiedValues: ElasticachePendingModifiedValues | None = None
    MemberClusters: list[StrictStr] | None = None