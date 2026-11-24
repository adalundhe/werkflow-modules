from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_findings_trends_string_filter import SecurityHubFindingsTrendsStringFilter


class SecurityHubFindingsTrendsCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubFindingsTrendsStringFilter] | None = None
    NestedCompositeFilters: list[SecurityHubFindingsTrendsCompositeFilter] | None = None
    Operator: Literal['AND', 'OR'] | None = None
