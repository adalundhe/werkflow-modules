from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeServerlessCacheSnapshotsRequest(BaseModel):
    ServerlessCacheName: StrictStr | None = None
    ServerlessCacheSnapshotName: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
