from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceDeploymentAlarms(BaseModel):
    status: StrictStr | None = None
    alarmNames: list[StrictStr] | None = None
    triggeredAlarmNames: list[StrictStr] | None = None
