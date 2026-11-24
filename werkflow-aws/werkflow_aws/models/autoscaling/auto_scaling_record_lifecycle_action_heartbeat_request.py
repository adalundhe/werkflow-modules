from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingRecordLifecycleActionHeartbeatRequest(BaseModel):
    LifecycleHookName: StrictStr
    AutoScalingGroupName: StrictStr
    LifecycleActionToken: StrictStr | None = None
    InstanceId: StrictStr | None = None
