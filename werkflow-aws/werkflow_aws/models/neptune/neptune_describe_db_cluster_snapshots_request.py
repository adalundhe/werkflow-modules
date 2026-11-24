from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeDBClusterSnapshotsRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    DBClusterSnapshotIdentifier: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Filters: list[NeptuneFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    IncludeShared: StrictBool | None = None
    IncludePublic: StrictBool | None = None
