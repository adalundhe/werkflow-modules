from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_auto_scaling_configuration import AppRunnerAutoScalingConfiguration


class AppRunnerDeleteAutoScalingConfigurationResponse(BaseModel):
    AutoScalingConfiguration: AppRunnerAutoScalingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
