from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeOrderableClusterOptionsRequest(BaseModel):
    ClusterVersion: StrictStr | None = None
    NodeType: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
