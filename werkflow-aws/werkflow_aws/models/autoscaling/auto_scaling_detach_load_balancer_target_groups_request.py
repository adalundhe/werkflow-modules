from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDetachLoadBalancerTargetGroupsRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TargetGroupARNs: list[StrictStr]
