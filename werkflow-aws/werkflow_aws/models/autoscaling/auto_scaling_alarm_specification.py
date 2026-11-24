from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAlarmSpecification(BaseModel):
    Alarms: list[StrictStr] | None = None
