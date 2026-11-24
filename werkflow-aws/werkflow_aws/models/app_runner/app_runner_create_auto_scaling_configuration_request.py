from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_runner_tag import AppRunnerTag


class AppRunnerCreateAutoScalingConfigurationRequest(BaseModel):
    AutoScalingConfigurationName: StrictStr
    MaxConcurrency: StrictInt | None = None
    MinSize: StrictInt | None = None
    MaxSize: StrictInt | None = None
    Tags: list[AppRunnerTag] | None = None
