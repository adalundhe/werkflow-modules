from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingLifecycleHookSpecification(BaseModel):
    LifecycleHookName: StrictStr
    LifecycleTransition: StrictStr
    NotificationMetadata: StrictStr | None = None
    HeartbeatTimeout: StrictInt | None = None
    DefaultResult: StrictStr | None = None
    NotificationTargetARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
