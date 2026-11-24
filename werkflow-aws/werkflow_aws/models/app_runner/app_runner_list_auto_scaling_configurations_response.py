from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_auto_scaling_configuration_summary import AppRunnerAutoScalingConfigurationSummary


class AppRunnerListAutoScalingConfigurationsResponse(BaseModel):
    AutoScalingConfigurationSummaryList: list[AppRunnerAutoScalingConfigurationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
