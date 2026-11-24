from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .security_hub_finding_scopes import SecurityHubFindingScopes
from .security_hub_group_by_rule import SecurityHubGroupByRule


class SecurityHubGetFindingStatisticsV2Request(BaseModel):
    GroupByRules: list[SecurityHubGroupByRule]
    Scopes: SecurityHubFindingScopes | None = None
    SortOrder: Literal['asc', 'desc'] | None = None
    MaxStatisticResults: StrictInt | None = None
