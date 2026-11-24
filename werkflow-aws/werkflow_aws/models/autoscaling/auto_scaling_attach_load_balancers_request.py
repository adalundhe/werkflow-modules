from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAttachLoadBalancersRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    LoadBalancerNames: list[StrictStr]
