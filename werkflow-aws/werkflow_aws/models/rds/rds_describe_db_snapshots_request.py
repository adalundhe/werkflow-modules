from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_filter import RDSFilter


class RDSDescribeDBSnapshotsRequest(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBSnapshotIdentifier: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Filters: list[RDSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    IncludeShared: StrictBool | None = None
    IncludePublic: StrictBool | None = None
    DbiResourceId: StrictStr | None = None
