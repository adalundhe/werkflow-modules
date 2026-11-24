from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_configuration_aggregator import ConfigServiceConfigurationAggregator


class ConfigServiceDescribeConfigurationAggregatorsResponse(BaseModel):
    ConfigurationAggregators: list[ConfigServiceConfigurationAggregator] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
