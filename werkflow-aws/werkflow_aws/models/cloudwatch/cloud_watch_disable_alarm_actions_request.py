from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDisableAlarmActionsRequest(BaseModel):
    AlarmNames: list[StrictStr]
