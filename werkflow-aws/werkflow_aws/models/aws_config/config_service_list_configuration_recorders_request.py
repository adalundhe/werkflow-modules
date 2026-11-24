from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_configuration_recorder_filter import ConfigServiceConfigurationRecorderFilter


class ConfigServiceListConfigurationRecordersRequest(BaseModel):
    Filters: list[ConfigServiceConfigurationRecorderFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
