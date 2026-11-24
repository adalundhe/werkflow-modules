from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElasticacheDescribeSnapshotsRequest(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    SnapshotName: StrictStr | None = None
    SnapshotSource: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    ShowNodeGroupConfig: StrictBool | None = None
