from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingCompleteLifecycleActionRequest(BaseModel):
    LifecycleHookName: StrictStr
    AutoScalingGroupName: StrictStr
    LifecycleActionResult: StrictStr
    LifecycleActionToken: StrictStr | None = None
    InstanceId: StrictStr | None = None
