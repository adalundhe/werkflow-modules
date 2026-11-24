from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAlarm(BaseModel):
    AlarmName: StrictStr | None = None
    AlarmARN: StrictStr | None = None
