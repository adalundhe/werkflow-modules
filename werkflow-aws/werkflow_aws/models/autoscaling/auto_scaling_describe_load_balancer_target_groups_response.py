from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_load_balancer_target_group_state import AutoScalingLoadBalancerTargetGroupState


class AutoScalingDescribeLoadBalancerTargetGroupsResponse(BaseModel):
    LoadBalancerTargetGroups: list[AutoScalingLoadBalancerTargetGroupState] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
