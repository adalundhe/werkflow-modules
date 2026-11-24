from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class AutoScalingDescribeAccountLimitsResponse(BaseModel):
    MaxNumberOfAutoScalingGroups: StrictInt | None = None
    MaxNumberOfLaunchConfigurations: StrictInt | None = None
    NumberOfAutoScalingGroups: StrictInt | None = None
    NumberOfLaunchConfigurations: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
