from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingCancelInstanceRefreshRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    WaitForTransitioningInstances: StrictBool | None = None
