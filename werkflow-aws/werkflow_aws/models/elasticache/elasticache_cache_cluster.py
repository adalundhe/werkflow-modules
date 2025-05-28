import datetime
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Literal
from .elasticache_endpoint import ElasticacheEndpoint
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration
from .elasticache_pending_modified_values import ElasticachePendingModifiedValues
from .elasticache_notification_configuration import ElasticacheNotificationConfiguration
from .elasticache_cache_secruity_group import ElasticacheCacheSecurityGroup
from .elasticache_cache_parameter_group import ElasticacheCacheParameterGroup
from .elasticache_cache_node import ElasticacheCacheNode
from .elasticache_security_group import ElasticacheSecurityGroup


class ElasticacheCacheCluster(BaseModel):
    CacheClusterId: StrictStr
    ConfigurationEndpoint: ElasticacheEndpoint
    ClientDownloadLandingPage: StrictStr
    Engine: StrictStr
    EngineVersion: StrictStr
    CacheClusterStatus: StrictStr
    NumCacheNodes: StrictInt
    PreferredAvailabilityZone: StrictStr
    PreferredOutpostArn: StrictStr
    CacheClusterCreateTime: datetime.datetime
    PreferredMaintenanceWindow: StrictStr
    PendingModifiedValues: ElasticachePendingModifiedValues
    NotificationConfiguration: ElasticacheNotificationConfiguration
    CacheSecurityGroups: list[ElasticacheCacheSecurityGroup]
    CacheParameterGroup: ElasticacheCacheParameterGroup
    CacheSubnetGroupName: StrictStr
    CacheNodes: list[ElasticacheCacheNode]
    AutoMinorVersionUpgrade: StrictBool
    SecurityGroups: list[ElasticacheSecurityGroup]
    ReplicationGroupId: StrictStr
    SnapshotRetentionLimit: StrictInt
    SnapshotWindow: StrictStr
    AuthTokenEnabled: StrictBool
    AuthTokenLastModifiedDate: datetime.datetime
    TransitEncryptionEnabled: StrictBool
    AtRestEncryptionEnabled: StrictBool
    ARN: StrictStr
    ReplicationGroupLogDeliveryEnabled: StrictBool
    LogDeliveryConfigurations: list[ElasticacheLogDeliveryConfiguration]
    NetworkType: Literal[
        'ipv4',
        'ipv6',
        'dual_stack',
    ]
    IpDiscovery: Literal[
        'ipv4',
        'ipv6',
    ]
    TransitEncryptionMode: Literal[
        'preferred',
        'required',
    ]