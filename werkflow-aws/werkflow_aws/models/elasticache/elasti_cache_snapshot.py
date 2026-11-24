from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_node_snapshot import ElastiCacheNodeSnapshot


class ElastiCacheSnapshot(BaseModel):
    SnapshotName: StrictStr | None = None
    ReplicationGroupId: StrictStr | None = None
    ReplicationGroupDescription: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    SnapshotStatus: StrictStr | None = None
    SnapshotSource: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    NumCacheNodes: StrictInt | None = None
    PreferredAvailabilityZone: StrictStr | None = None
    PreferredOutpostArn: StrictStr | None = None
    CacheClusterCreateTime: datetime.datetime | StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    TopicArn: StrictStr | None = None
    Port: StrictInt | None = None
    CacheParameterGroupName: StrictStr | None = None
    CacheSubnetGroupName: StrictStr | None = None
    VpcId: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    NumNodeGroups: StrictInt | None = None
    AutomaticFailover: StrictStr | None = None
    NodeSnapshots: list[ElastiCacheNodeSnapshot] | None = None
    KmsKeyId: StrictStr | None = None
    ARN: StrictStr | None = None
    DataTiering: StrictStr | None = None
    Durability: StrictStr | None = None
