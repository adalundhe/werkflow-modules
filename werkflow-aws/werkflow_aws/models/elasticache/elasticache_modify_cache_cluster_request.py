from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElasticacheModifyCacheClusterRequest(BaseModel):
    CacheClusterId: StrictStr
    NumCacheNodes: StrictInt | None = None
    CacheNodeIdsToRemove: list[StrictStr] | None = None
    AZMode: StrictStr | None = None
    NewAvailabilityZones: list[StrictStr] | None = None
    CacheSecurityGroupNames: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    NotificationTopicArn: StrictStr | None = None
    CacheParameterGroupName: StrictStr | None = None
    ApplyImmediately: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    SnapshotRetentionLimit: StrictInt | None = None
    SnapshotWindow: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
