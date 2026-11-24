from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasticache_automatic_failover import ElasticacheAutomaticFailover
from .elasticache_cluster_mode import ElasticacheClusterMode
from .elasticache_data_tiering import ElasticacheDataTiering
from .elasticache_endpoint import ElasticacheEndpoint
from .elasticache_ip_discovery import ElasticacheIpDiscovery
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration
from .elasticache_multi_az import ElasticacheMultiAZ
from .elasticache_network_type import ElasticacheNetworkType
from .elasticache_node_group_member import ElasticacheNodeGroupMember
from .elasticache_transit_encryption_mode import ElasticacheTransitEncryptionMode


class ElasticacheNodeGroup(BaseModel):
    NodeGroupId: StrictStr
    Status: StrictStr
    PrimaryEndpoint: ElasticacheEndpoint
    ReaderEndpoint: ElasticacheEndpoint
    Slots: StrictStr
    NodeGroupMembers: list[ElasticacheNodeGroupMember] | None = None
    SnapshottingClusterId: StrictStr
    AutomaticFailover: ElasticacheAutomaticFailover
    MultiAZ: ElasticacheMultiAZ
    ConfigurationEndpoint: ElasticacheEndpoint
    SnapshotRetentionLimit: StrictInt
    SnapshotWindow: StrictStr
    ClusterEnabled: StrictBool = True
    CacheNodeType: StrictStr
    AuthTokenEnabled: StrictBool = False
    AuthTokenLastModifiedDate: datetime.datetime
    TransitEncryptionEnabled: StrictBool = False
    AtRestEncryptionEnabled: StrictBool = False
    MemberClusterOutpostArns: list[StrictStr] | None = None
    KmsKeyId: StrictStr
    ARN: StrictStr
    UserGroupIds: list[StrictStr] | None = None
    LogDeliveryConfigurations: list[ElasticacheLogDeliveryConfiguration] | None = None
    ReplicationGroupCreateTime: datetime.datetime
    DataTiering: ElasticacheDataTiering
    AutoMinorVersionUpgrade: StrictBool = False
    NetworkType: ElasticacheNetworkType
    IpDiscovery: ElasticacheIpDiscovery
    TransitEncryptionMode: ElasticacheTransitEncryptionMode
    ClusterMode: ElasticacheClusterMode
