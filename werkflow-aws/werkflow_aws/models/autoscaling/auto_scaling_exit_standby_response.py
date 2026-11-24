from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_activity import AutoScalingActivity


class AutoScalingExitStandbyResponse(BaseModel):
    Activities: list[AutoScalingActivity] | None = None
    ResponseMetadata: dict[str, Any] | None = None
