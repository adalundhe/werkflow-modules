from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_retention_configuration import ConfigServiceRetentionConfiguration


class ConfigServicePutRetentionConfigurationResponse(BaseModel):
    RetentionConfiguration: ConfigServiceRetentionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
