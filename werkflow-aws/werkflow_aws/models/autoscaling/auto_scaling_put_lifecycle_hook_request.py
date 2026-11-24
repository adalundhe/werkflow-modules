from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingPutLifecycleHookRequest(BaseModel):
    LifecycleHookName: StrictStr
    AutoScalingGroupName: StrictStr
    LifecycleTransition: StrictStr | None = None
    RoleARN: StrictStr | None = None
    NotificationTargetARN: StrictStr | None = None
    NotificationMetadata: StrictStr | None = None
    HeartbeatTimeout: StrictInt | None = None
    DefaultResult: StrictStr | None = None
