from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAttachInstancesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    InstanceIds: list[StrictStr] | None = None
