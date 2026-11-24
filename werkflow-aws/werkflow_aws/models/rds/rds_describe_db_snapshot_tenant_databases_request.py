from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeDBSnapshotTenantDatabasesRequest(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBSnapshotIdentifier: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
