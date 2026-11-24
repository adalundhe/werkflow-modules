from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingDetachInstancesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ShouldDecrementDesiredCapacity: StrictBool
    InstanceIds: list[StrictStr] | None = None
