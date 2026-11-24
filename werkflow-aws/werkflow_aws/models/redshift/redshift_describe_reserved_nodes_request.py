from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeReservedNodesRequest(BaseModel):
    ReservedNodeId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
