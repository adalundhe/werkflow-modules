from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingEnterStandbyRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ShouldDecrementDesiredCapacity: StrictBool
    InstanceIds: list[StrictStr] | None = None
