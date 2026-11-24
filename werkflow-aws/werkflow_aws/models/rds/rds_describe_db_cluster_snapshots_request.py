from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter import RDSFilter


class RDSDescribeDBClusterSnapshotsRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    DBClusterSnapshotIdentifier: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Filters: list[RDSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    IncludeShared: StrictBool | None = None
    IncludePublic: StrictBool | None = None
    DbClusterResourceId: StrictStr | None = None
