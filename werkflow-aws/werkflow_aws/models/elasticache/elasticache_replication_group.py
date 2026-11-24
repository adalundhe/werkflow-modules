from pydantic import BaseModel, StrictBool, StrictStr
from .elasticache_global_replication_group_info import ElasticacheGlobalReplicationGroupInfo
from .elasticache_node_group import ElasticacheNodeGroup
from .elasticache_pending_modified_values import ElasticachePendingModifiedValues


class ElasticacheReplicationGroup(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    Description: StrictStr | None = None
    GlobalReplicationGroupInfo: ElasticacheGlobalReplicationGroupInfo | None = None
    Status: StrictStr | None = None
    PendingModifiedValues: ElasticachePendingModifiedValues | None = None
    MemberClusters: list[StrictStr] | None = None
    NodeGroups: list[ElasticacheNodeGroup] | None = None
    AutomaticFailover: StrictStr | None = None
    MultiAZ: StrictStr | None = None
    ARN: StrictStr | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    AtRestEncryptionEnabled: StrictBool | None = None
    ClusterEnabled: StrictBool | None = None
