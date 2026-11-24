from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_software_filters import SecurityHubSoftwareFilters
from .security_hub_software_scopes import SecurityHubSoftwareScopes
from .security_hub_sort_criterion import SecurityHubSortCriterion


class SecurityHubGetSoftwareV2Request(BaseModel):
    Filters: SecurityHubSoftwareFilters | None = None
    Scopes: SecurityHubSoftwareScopes | None = None
    SortCriteria: list[SecurityHubSortCriterion] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
