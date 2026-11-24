from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDeleteLifecycleHookRequest(BaseModel):
    LifecycleHookName: StrictStr
    AutoScalingGroupName: StrictStr
