from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_instance_refresh import AutoScalingInstanceRefresh


class AutoScalingDescribeInstanceRefreshesResponse(BaseModel):
    InstanceRefreshes: list[AutoScalingInstanceRefresh] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
