from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_instance_details import AutoScalingInstanceDetails


class AutoScalingDescribeAutoScalingInstancesResponse(BaseModel):
    AutoScalingInstances: list[AutoScalingInstanceDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
