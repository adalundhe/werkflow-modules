from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_configuration_recorder_status import ConfigServiceConfigurationRecorderStatus


class ConfigServiceDescribeConfigurationRecorderStatusResponse(BaseModel):
    ConfigurationRecordersStatus: list[ConfigServiceConfigurationRecorderStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
