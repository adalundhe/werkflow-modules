from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDaemonAlarmConfiguration(BaseModel):
    alarmNames: list[StrictStr] | None = None
    enable: StrictBool | None = None
