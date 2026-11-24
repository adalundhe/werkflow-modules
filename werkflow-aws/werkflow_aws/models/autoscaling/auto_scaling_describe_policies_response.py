from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_scaling_policy import AutoScalingScalingPolicy


class AutoScalingDescribePoliciesResponse(BaseModel):
    ScalingPolicies: list[AutoScalingScalingPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
