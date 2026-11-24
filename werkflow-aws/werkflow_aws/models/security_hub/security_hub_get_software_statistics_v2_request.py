from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .security_hub_software_group_by_rule import SecurityHubSoftwareGroupByRule
from .security_hub_software_scopes import SecurityHubSoftwareScopes


class SecurityHubGetSoftwareStatisticsV2Request(BaseModel):
    GroupByRules: list[SecurityHubSoftwareGroupByRule]
    Scopes: SecurityHubSoftwareScopes | None = None
    SortOrder: Literal['asc', 'desc'] | None = None
    MaxStatisticResults: StrictInt | None = None
