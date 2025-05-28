import datetime
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Literal
from .elasticache_endpoint import ElasticacheEndpoint
from .elasticache_node_group_member import ElasticacheNodeGroupMember
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration

ElasticacheAutomaticFailover = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
]

ElasticacheMultiAZ = Literal[
    "enabled",
    "disabled",
]

ElasticacheDataTiering = Literal[
    "enabled",
    "disabled"
]

ElasticacheNetworkType = Literal[
    "ipv4",
    "ipv6",
    "dual_stack",
]

ElasticacheIpDiscovery = Literal[
    "ipv4",
    "ipv6"
]

ElasticacheTransitEncryptionMode = Literal[
    "preferred",
    "required",
]

ElasticacheClusterMode = Literal[
    "enabled",
    "disabled",
    "compatible"
]


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

