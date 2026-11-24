from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteSnapshotScheduleRequest(BaseModel):
    ScheduleIdentifier: StrictStr
