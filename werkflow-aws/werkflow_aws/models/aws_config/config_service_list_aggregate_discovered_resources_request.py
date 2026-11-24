from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_resource_filters import ConfigServiceResourceFilters


class ConfigServiceListAggregateDiscoveredResourcesRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    ResourceType: StrictStr
    Filters: ConfigServiceResourceFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
