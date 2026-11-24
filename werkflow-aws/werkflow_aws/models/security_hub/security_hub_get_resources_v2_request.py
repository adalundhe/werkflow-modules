from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_resource_scopes import SecurityHubResourceScopes
from .security_hub_resources_filters import SecurityHubResourcesFilters
from .security_hub_sort_criterion import SecurityHubSortCriterion


class SecurityHubGetResourcesV2Request(BaseModel):
    Filters: SecurityHubResourcesFilters | None = None
    Scopes: SecurityHubResourceScopes | None = None
    SortCriteria: list[SecurityHubSortCriterion] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
