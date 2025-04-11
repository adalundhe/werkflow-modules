import datetime
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Literal
from .configuration_endpoint import ConfigurationEndpoint
from .log_delivery_configuration import LogDeliveryConfiguration
from .pending_modified_values import PendingModifiedValues
from .notification_configuration import NotificationConfiguration
from .cache_secruity_group import CacheSecurityGroup
from .cache_parameter_group import CacheParameterGroup
from .cache_node import CacheNode
from .security_group import SecurityGroup


class CacheCluster(BaseModel):
    CacheClusterId: StrictStr
    ConfigurationEndpoint: ConfigurationEndpoint
    ClientDownloadLandingPage: StrictStr
    Engine: StrictStr
    EngineVersion: StrictStr
    CacheClusterStatus: StrictStr
    NumCacheNodes: StrictInt
    PreferredAvailabilityZone: StrictStr
    PreferredOutpostArn: StrictStr
    CacheClusterCreateTime: datetime.datetime
    PreferredMaintenanceWindow: StrictStr
    PendingModifiedValues: PendingModifiedValues
    NotificationConfiguration: NotificationConfiguration
    CacheSecurityGroups: list[CacheSecurityGroup]
    CacheParameterGroup: CacheParameterGroup
    CacheSubnetGroupName: StrictStr
    CacheNodes: list[CacheNode]
    AutoMinorVersionUpgrade: StrictBool
    SecurityGroups: list[SecurityGroup]
    ReplicationGroupId: StrictStr
    SnapshotRetentionLimit: StrictInt
    SnapshotWindow: StrictStr
    AuthTokenEnabled: StrictBool
    AuthTokenLastModifiedDate: datetime.datetime
    TransitEncryptionEnabled: StrictBool
    AtRestEncryptionEnabled: StrictBool
    ARN: StrictStr
    ReplicationGroupLogDeliveryEnabled: StrictBool
    LogDeliveryConfigurations: list[LogDeliveryConfiguration]
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