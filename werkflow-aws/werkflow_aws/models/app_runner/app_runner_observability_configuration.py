from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_runner_trace_configuration import AppRunnerTraceConfiguration


class AppRunnerObservabilityConfiguration(BaseModel):
    ObservabilityConfigurationArn: StrictStr | None = None
    ObservabilityConfigurationName: StrictStr | None = None
    TraceConfiguration: AppRunnerTraceConfiguration | None = None
    ObservabilityConfigurationRevision: StrictInt | None = None
    Latest: StrictBool | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    DeletedAt: datetime.datetime | StrictStr | None = None
