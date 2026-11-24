from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_observability_configuration_summary import AppRunnerObservabilityConfigurationSummary


class AppRunnerListObservabilityConfigurationsResponse(BaseModel):
    ObservabilityConfigurationSummaryList: list[AppRunnerObservabilityConfigurationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
