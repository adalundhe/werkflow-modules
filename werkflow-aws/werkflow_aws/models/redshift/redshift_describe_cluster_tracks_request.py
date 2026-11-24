from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeClusterTracksRequest(BaseModel):
    MaintenanceTrackName: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
