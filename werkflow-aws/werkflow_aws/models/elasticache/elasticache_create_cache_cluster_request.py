from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasticache_tag import ElasticacheTag


class ElasticacheCreateCacheClusterRequest(BaseModel):
    CacheClusterId: StrictStr
    ReplicationGroupId: StrictStr | None = None
    AZMode: StrictStr | None = None
    PreferredAvailabilityZone: StrictStr | None = None
    PreferredAvailabilityZones: list[StrictStr] | None = None
    NumCacheNodes: StrictInt | None = None
    CacheNodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheParameterGroupName: StrictStr | None = None
    CacheSubnetGroupName: StrictStr | None = None
    CacheSecurityGroupNames: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[ElasticacheTag] | None = None
    SnapshotArns: list[StrictStr] | None = None
    SnapshotName: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    Port: StrictInt | None = None
    NotificationTopicArn: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    AuthToken: StrictStr | None = None
    TransitEncryptionEnabled: StrictBool | None = None
