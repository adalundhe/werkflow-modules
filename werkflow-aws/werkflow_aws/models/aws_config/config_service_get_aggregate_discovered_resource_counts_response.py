from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_grouped_resource_count import ConfigServiceGroupedResourceCount


class ConfigServiceGetAggregateDiscoveredResourceCountsResponse(BaseModel):
    TotalDiscoveredResources: StrictInt | None = None
    GroupByKey: StrictStr | None = None
    GroupedResourceCounts: list[ConfigServiceGroupedResourceCount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
