from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class AutoScalingCreateLaunchConfigurationResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
