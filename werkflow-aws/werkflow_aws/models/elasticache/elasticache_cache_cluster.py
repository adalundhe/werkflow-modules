import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasticache_cache_node import ElasticacheCacheNode
from .elasticache_cache_parameter_group import ElasticacheCacheParameterGroup
from .elasticache_cache_secruity_group import ElasticacheCacheSecurityGroup
from .elasticache_endpoint import ElasticacheEndpoint
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration
from .elasticache_notification_configuration import ElasticacheNotificationConfiguration
from .elasticache_pending_modified_values import ElasticachePendingModifiedValues
from .elasticache_security_group import ElasticacheSecurityGroup


class ElasticacheCacheCluster(BaseModel):
    CacheClusterId: StrictStr | None = None
    ConfigurationEndpoint: ElasticacheEndpoint | None = None
    ClientDownloadLandingPage: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheClusterStatus: StrictStr | None = None
    NumCacheNodes: StrictInt | None = None
    PreferredAvailabilityZone: StrictStr | None = None
    PreferredOutpostArn: StrictStr | None = None
    CacheClusterCreateTime: datetime.datetime | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: ElasticachePendingModifiedValues | None = None
    NotificationConfiguration: ElasticacheNotificationConfiguration | None = None
    CacheSecurityGroups: list[ElasticacheCacheSecurityGroup] | None = None
    CacheParameterGroup: ElasticacheCacheParameterGroup | None = None
    CacheSubnetGroupName: StrictStr | None = None
    CacheNodes: list[ElasticacheCacheNode] | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SecurityGroups: list[ElasticacheSecurityGroup] | None = None
    ReplicationGroupId: StrictStr | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    AuthTokenEnabled: StrictBool | None = None
    AuthTokenLastModifiedDate: datetime.datetime | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    AtRestEncryptionEnabled: StrictBool | None = None
    ARN: StrictStr | None = None
    ReplicationGroupLogDeliveryEnabled: StrictBool | None = None
    LogDeliveryConfigurations: list[ElasticacheLogDeliveryConfiguration] | None = None
    NetworkType: Literal['ipv4', 'ipv6', 'dual_stack'] | None = None
    IpDiscovery: Literal['ipv4', 'ipv6'] | None = None
    TransitEncryptionMode: Literal['preferred', 'required'] | None = None
