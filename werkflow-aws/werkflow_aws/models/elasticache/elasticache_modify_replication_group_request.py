from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElasticacheModifyReplicationGroupRequest(BaseModel):
    ReplicationGroupId: StrictStr
    ReplicationGroupDescription: StrictStr | None = None
    PrimaryClusterId: StrictStr | None = None
    SnapshottingClusterId: StrictStr | None = None
    AutomaticFailoverEnabled: StrictBool | None = None
    MultiAZEnabled: StrictBool | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    CacheParameterGroupName: StrictStr | None = None
    ApplyImmediately: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
