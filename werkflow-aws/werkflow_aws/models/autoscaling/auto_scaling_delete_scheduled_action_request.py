from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDeleteScheduledActionRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ScheduledActionName: StrictStr
