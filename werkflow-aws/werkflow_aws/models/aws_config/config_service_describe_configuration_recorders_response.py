from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_configuration_recorder import ConfigServiceConfigurationRecorder


class ConfigServiceDescribeConfigurationRecordersResponse(BaseModel):
    ConfigurationRecorders: list[ConfigServiceConfigurationRecorder] | None = None
    ResponseMetadata: dict[str, Any] | None = None
