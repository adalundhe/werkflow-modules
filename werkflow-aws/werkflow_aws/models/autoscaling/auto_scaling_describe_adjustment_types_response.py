from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_adjustment_type import AutoScalingAdjustmentType


class AutoScalingDescribeAdjustmentTypesResponse(BaseModel):
    AdjustmentTypes: list[AutoScalingAdjustmentType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
