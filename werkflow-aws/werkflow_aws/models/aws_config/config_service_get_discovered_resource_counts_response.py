from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_resource_count import ConfigServiceResourceCount


class ConfigServiceGetDiscoveredResourceCountsResponse(BaseModel):
    totalDiscoveredResources: StrictInt | None = None
    resourceCounts: list[ConfigServiceResourceCount] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
