from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingLifecycleHook(BaseModel):
    LifecycleHookName: StrictStr | None = None
    AutoScalingGroupName: StrictStr | None = None
    LifecycleTransition: StrictStr | None = None
    NotificationTargetARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
    NotificationMetadata: StrictStr | None = None
    HeartbeatTimeout: StrictInt | None = None
    GlobalTimeout: StrictInt | None = None
    DefaultResult: StrictStr | None = None
