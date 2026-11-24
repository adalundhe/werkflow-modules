from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MemoryDBDescribeSnapshotsRequest(BaseModel):
    ClusterName: StrictStr | None = None
    SnapshotName: StrictStr | None = None
    Source: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ShowDetail: StrictBool | None = None
