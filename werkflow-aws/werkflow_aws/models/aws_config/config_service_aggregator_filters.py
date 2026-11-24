from __future__ import annotations
from pydantic import BaseModel
from .config_service_aggregator_filter_resource_type import ConfigServiceAggregatorFilterResourceType
from .config_service_aggregator_filter_service_principal import ConfigServiceAggregatorFilterServicePrincipal


class ConfigServiceAggregatorFilters(BaseModel):
    ResourceType: ConfigServiceAggregatorFilterResourceType | None = None
    ServicePrincipal: ConfigServiceAggregatorFilterServicePrincipal | None = None
