from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_observability_configuration import AppRunnerObservabilityConfiguration


class AppRunnerDeleteObservabilityConfigurationResponse(BaseModel):
    ObservabilityConfiguration: AppRunnerObservabilityConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
