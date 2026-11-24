from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDescribeLifecycleHooksRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    LifecycleHookNames: list[StrictStr] | None = None
