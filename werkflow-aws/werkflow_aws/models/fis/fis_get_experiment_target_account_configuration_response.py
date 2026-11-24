from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_experiment_target_account_configuration import FISExperimentTargetAccountConfiguration


class FISGetExperimentTargetAccountConfigurationResponse(BaseModel):
    targetAccountConfiguration: FISExperimentTargetAccountConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
