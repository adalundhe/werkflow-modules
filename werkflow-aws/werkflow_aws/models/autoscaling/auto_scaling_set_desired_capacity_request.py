from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingSetDesiredCapacityRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    DesiredCapacity: StrictInt
    HonorCooldown: StrictBool | None = None
