from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_process_type import AutoScalingProcessType


class AutoScalingDescribeScalingProcessTypesResponse(BaseModel):
    Processes: list[AutoScalingProcessType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
