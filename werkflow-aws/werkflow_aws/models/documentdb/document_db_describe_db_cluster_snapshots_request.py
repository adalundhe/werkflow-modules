from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeDBClusterSnapshotsRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    DBClusterSnapshotIdentifier: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    IncludeShared: StrictBool | None = None
    IncludePublic: StrictBool | None = None
