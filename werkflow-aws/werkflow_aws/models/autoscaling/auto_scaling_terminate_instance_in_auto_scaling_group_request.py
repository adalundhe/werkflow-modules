from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingTerminateInstanceInAutoScalingGroupRequest(BaseModel):
    ShouldDecrementDesiredCapacity: StrictBool
    InstanceId: StrictStr | None = None
    InstanceIds: list[StrictStr] | None = None
    AutoScalingGroupName: StrictStr | None = None
