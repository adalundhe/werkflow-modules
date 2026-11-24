from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_filter import RDSFilter


class RDSDescribeDBInstancesRequest(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    Filters: list[RDSFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
