from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_flywheel_iteration_properties import ComprehendFlywheelIterationProperties


class ComprehendDescribeFlywheelIterationResponse(BaseModel):
    FlywheelIterationProperties: ComprehendFlywheelIterationProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
