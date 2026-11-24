from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeTableRestoreStatusRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    TableRestoreRequestId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
