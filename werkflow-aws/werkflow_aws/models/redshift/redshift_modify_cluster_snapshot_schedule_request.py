from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftModifyClusterSnapshotScheduleRequest(BaseModel):
    ClusterIdentifier: StrictStr
    ScheduleIdentifier: StrictStr | None = None
    DisassociateSchedule: StrictBool | None = None
