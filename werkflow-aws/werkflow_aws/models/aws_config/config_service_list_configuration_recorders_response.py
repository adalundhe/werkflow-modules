from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_configuration_recorder_summary import ConfigServiceConfigurationRecorderSummary


class ConfigServiceListConfigurationRecordersResponse(BaseModel):
    ConfigurationRecorderSummaries: list[ConfigServiceConfigurationRecorderSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
