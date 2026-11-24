from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingExitStandbyRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    InstanceIds: list[StrictStr] | None = None
