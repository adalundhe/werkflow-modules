from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_configuration_aggregator import ConfigServiceConfigurationAggregator


class ConfigServicePutConfigurationAggregatorResponse(BaseModel):
    ConfigurationAggregator: ConfigServiceConfigurationAggregator | None = None
    ResponseMetadata: dict[str, Any] | None = None
