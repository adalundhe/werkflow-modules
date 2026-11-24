from __future__ import annotations
from pydantic import BaseModel
from .config_service_configuration_recorder import ConfigServiceConfigurationRecorder
from .config_service_tag import ConfigServiceTag


class ConfigServicePutConfigurationRecorderRequest(BaseModel):
    ConfigurationRecorder: ConfigServiceConfigurationRecorder
    Tags: list[ConfigServiceTag] | None = None
