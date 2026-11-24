from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_configuration_item import ConfigServiceConfigurationItem


class ConfigServiceGetResourceConfigHistoryResponse(BaseModel):
    configurationItems: list[ConfigServiceConfigurationItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
