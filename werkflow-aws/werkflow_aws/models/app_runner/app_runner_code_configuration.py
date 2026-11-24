from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_code_configuration_values import AppRunnerCodeConfigurationValues


class AppRunnerCodeConfiguration(BaseModel):
    ConfigurationSource: StrictStr | None = None
    CodeConfigurationValues: AppRunnerCodeConfigurationValues | None = None
