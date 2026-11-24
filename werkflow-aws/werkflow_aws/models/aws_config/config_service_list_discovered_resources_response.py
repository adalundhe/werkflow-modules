from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_resource_identifier import ConfigServiceResourceIdentifier


class ConfigServiceListDiscoveredResourcesResponse(BaseModel):
    resourceIdentifiers: list[ConfigServiceResourceIdentifier] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
