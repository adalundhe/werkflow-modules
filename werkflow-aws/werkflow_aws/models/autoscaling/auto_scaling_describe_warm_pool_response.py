from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_instance import AutoScalingInstance
from .auto_scaling_warm_pool_configuration import AutoScalingWarmPoolConfiguration


class AutoScalingDescribeWarmPoolResponse(BaseModel):
    WarmPoolConfiguration: AutoScalingWarmPoolConfiguration | None = None
    Instances: list[AutoScalingInstance] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
