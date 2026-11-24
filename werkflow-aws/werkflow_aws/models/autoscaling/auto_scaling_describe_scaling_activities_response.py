from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_activity import AutoScalingActivity


class AutoScalingDescribeScalingActivitiesResponse(BaseModel):
    Activities: list[AutoScalingActivity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
