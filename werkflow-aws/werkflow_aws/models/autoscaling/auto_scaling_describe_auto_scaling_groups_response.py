from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_group import AutoScalingGroup


class AutoScalingDescribeAutoScalingGroupsResponse(BaseModel):
    AutoScalingGroups: list[AutoScalingGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
