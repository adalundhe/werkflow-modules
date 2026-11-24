from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeSnapshotSchedulesRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    ScheduleIdentifier: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
    TagValues: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
