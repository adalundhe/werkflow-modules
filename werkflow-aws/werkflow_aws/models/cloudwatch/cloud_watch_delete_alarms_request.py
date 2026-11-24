from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDeleteAlarmsRequest(BaseModel):
    AlarmNames: list[StrictStr] | None = None
