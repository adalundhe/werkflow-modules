from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifySnapshotScheduleRequest(BaseModel):
    ScheduleIdentifier: StrictStr
    ScheduleDefinitions: list[StrictStr]
