from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_load_balancer_state import AutoScalingLoadBalancerState


class AutoScalingDescribeLoadBalancersResponse(BaseModel):
    LoadBalancers: list[AutoScalingLoadBalancerState] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
