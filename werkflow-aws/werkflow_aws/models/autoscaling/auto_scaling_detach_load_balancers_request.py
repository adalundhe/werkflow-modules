from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDetachLoadBalancersRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    LoadBalancerNames: list[StrictStr]
