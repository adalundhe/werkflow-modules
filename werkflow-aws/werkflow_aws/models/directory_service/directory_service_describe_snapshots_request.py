from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeSnapshotsRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    SnapshotIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
