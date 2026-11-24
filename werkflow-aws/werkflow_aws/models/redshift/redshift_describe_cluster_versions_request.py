from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeClusterVersionsRequest(BaseModel):
    ClusterVersion: StrictStr | None = None
    ClusterParameterGroupFamily: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
