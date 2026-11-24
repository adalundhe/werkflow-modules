from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAttachLoadBalancerTargetGroupsRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TargetGroupARNs: list[StrictStr]
