from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasticache_tag import ElasticacheTag


class ElasticacheCreateReplicationGroupRequest(BaseModel):
    ReplicationGroupId: StrictStr
    ReplicationGroupDescription: StrictStr
    PrimaryClusterId: StrictStr | None = None
    AutomaticFailoverEnabled: StrictBool | None = None
    MultiAZEnabled: StrictBool | None = None
    NumCacheClusters: StrictInt | None = None
    PreferredCacheClusterAZs: list[StrictStr] | None = None
    NumNodeGroups: StrictInt | None = None
    ReplicasPerNodeGroup: StrictInt | None = None
    CacheNodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheParameterGroupName: StrictStr | None = None
    CacheSubnetGroupName: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[ElasticacheTag] | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    Port: StrictInt | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    AuthToken: StrictStr | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    AtRestEncryptionEnabled: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
