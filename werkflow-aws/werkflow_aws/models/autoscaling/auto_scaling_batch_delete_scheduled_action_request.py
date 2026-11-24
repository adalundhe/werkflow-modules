from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingBatchDeleteScheduledActionRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ScheduledActionNames: list[StrictStr]
