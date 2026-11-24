from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_target_account_configuration_summary import FISTargetAccountConfigurationSummary


class FISListTargetAccountConfigurationsResponse(BaseModel):
    targetAccountConfigurations: list[FISTargetAccountConfigurationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
