from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_base_configuration_item import ConfigServiceBaseConfigurationItem
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceBatchGetResourceConfigResponse(BaseModel):
    baseConfigurationItems: list[ConfigServiceBaseConfigurationItem] | None = None
    unprocessedResourceKeys: list[ConfigServiceResourceKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
