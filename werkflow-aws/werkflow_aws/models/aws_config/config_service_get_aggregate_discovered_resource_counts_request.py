from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_resource_count_filters import ConfigServiceResourceCountFilters


class ConfigServiceGetAggregateDiscoveredResourceCountsRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    Filters: ConfigServiceResourceCountFilters | None = None
    GroupByKey: Literal['RESOURCE_TYPE', 'ACCOUNT_ID', 'AWS_REGION'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
