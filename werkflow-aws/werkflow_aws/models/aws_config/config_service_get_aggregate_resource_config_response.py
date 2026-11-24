from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_configuration_item import ConfigServiceConfigurationItem


class ConfigServiceGetAggregateResourceConfigResponse(BaseModel):
    ConfigurationItem: ConfigServiceConfigurationItem | None = None
    ResponseMetadata: dict[str, Any] | None = None
