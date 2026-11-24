from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_aggregate_resource_identifier import ConfigServiceAggregateResourceIdentifier
from .config_service_base_configuration_item import ConfigServiceBaseConfigurationItem


class ConfigServiceBatchGetAggregateResourceConfigResponse(BaseModel):
    BaseConfigurationItems: list[ConfigServiceBaseConfigurationItem] | None = None
    UnprocessedResourceIdentifiers: list[ConfigServiceAggregateResourceIdentifier] | None = None
    ResponseMetadata: dict[str, Any] | None = None
