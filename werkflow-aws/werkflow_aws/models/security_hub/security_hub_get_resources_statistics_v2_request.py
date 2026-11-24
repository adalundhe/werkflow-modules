from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .security_hub_resource_group_by_rule import SecurityHubResourceGroupByRule
from .security_hub_resource_scopes import SecurityHubResourceScopes


class SecurityHubGetResourcesStatisticsV2Request(BaseModel):
    GroupByRules: list[SecurityHubResourceGroupByRule]
    Scopes: SecurityHubResourceScopes | None = None
    SortOrder: Literal['asc', 'desc'] | None = None
    MaxStatisticResults: StrictInt | None = None
