from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Any


class ElasticacheSnapshot(BaseModel):
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
    CacheClusterCreateTime: datetime.datetime | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    ARN: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    NodeSnapshots: list[dict[str, Any]] | None = None
