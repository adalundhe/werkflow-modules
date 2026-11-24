from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_tag import AppRunnerTag
from .app_runner_trace_configuration import AppRunnerTraceConfiguration


class AppRunnerCreateObservabilityConfigurationRequest(BaseModel):
    ObservabilityConfigurationName: StrictStr
    TraceConfiguration: AppRunnerTraceConfiguration | None = None
    Tags: list[AppRunnerTag] | None = None
