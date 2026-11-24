from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeDBClustersRequest(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    Filters: list[NeptuneFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
