from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_snapshot_schedule import RedshiftSnapshotSchedule


class RedshiftDescribeSnapshotSchedulesResponse(BaseModel):
    SnapshotSchedules: list[RedshiftSnapshotSchedule] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
