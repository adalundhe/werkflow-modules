from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_finding_scopes import SecurityHubFindingScopes
from .security_hub_ocsf_finding_filters import SecurityHubOcsfFindingFilters
from .security_hub_sort_criterion import SecurityHubSortCriterion


class SecurityHubGetFindingsV2Request(BaseModel):
    Filters: SecurityHubOcsfFindingFilters | None = None
    Scopes: SecurityHubFindingScopes | None = None
    SortCriteria: list[SecurityHubSortCriterion] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
