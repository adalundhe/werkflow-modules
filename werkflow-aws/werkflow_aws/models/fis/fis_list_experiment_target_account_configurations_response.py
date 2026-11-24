from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_experiment_target_account_configuration_summary import FISExperimentTargetAccountConfigurationSummary


class FISListExperimentTargetAccountConfigurationsResponse(BaseModel):
    targetAccountConfigurations: list[FISExperimentTargetAccountConfigurationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
