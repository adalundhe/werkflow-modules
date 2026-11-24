from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_snapshot_filter import FSxSnapshotFilter


class FSxDescribeSnapshotsRequest(BaseModel):
    SnapshotIds: list[StrictStr] | None = None
    Filters: list[FSxSnapshotFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    IncludeShared: StrictBool | None = None
