from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_endpoint import ElastiCacheEndpoint
from .elasti_cache_global_replication_group_info import ElastiCacheGlobalReplicationGroupInfo
from .elasti_cache_log_delivery_configuration import ElastiCacheLogDeliveryConfiguration
from .elasti_cache_node_group import ElastiCacheNodeGroup
from .elasti_cache_replication_group_pending_modified_values import ElastiCacheReplicationGroupPendingModifiedValues


class ElastiCacheReplicationGroup(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    Description: StrictStr | None = None
    GlobalReplicationGroupInfo: ElastiCacheGlobalReplicationGroupInfo | None = None
    Status: StrictStr | None = None
    PendingModifiedValues: ElastiCacheReplicationGroupPendingModifiedValues | None = None
    MemberClusters: list[StrictStr] | None = None
    NodeGroups: list[ElastiCacheNodeGroup] | None = None
    SnapshottingClusterId: StrictStr | None = None
    AutomaticFailover: StrictStr | None = None
    MultiAZ: StrictStr | None = None
    ConfigurationEndpoint: ElastiCacheEndpoint | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    ClusterEnabled: StrictBool | None = None
    CacheNodeType: StrictStr | None = None
    AuthTokenEnabled: StrictBool | None = None
    AuthTokenLastModifiedDate: datetime.datetime | StrictStr | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    AtRestEncryptionEnabled: StrictBool | None = None
    MemberClustersOutpostArns: list[StrictStr] | None = None
    KmsKeyId: StrictStr | None = None
    StorageEncryptionType: StrictStr | None = None
    ARN: StrictStr | None = None
    UserGroupIds: list[StrictStr] | None = None
    LogDeliveryConfigurations: list[ElastiCacheLogDeliveryConfiguration] | None = None
    ReplicationGroupCreateTime: datetime.datetime | StrictStr | None = None
    DataTiering: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    NetworkType: StrictStr | None = None
    IpDiscovery: StrictStr | None = None
    TransitEncryptionMode: StrictStr | None = None
    ClusterMode: StrictStr | None = None
    Engine: StrictStr | None = None
    Durability: StrictStr | None = None
    EffectiveDurability: StrictStr | None = None
