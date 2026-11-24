from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDeploymentAlarms(BaseModel):
    alarmNames: list[StrictStr] | None = None
    rollback: StrictBool | None = None
    enable: StrictBool | None = None
