from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_resources_trends_string_filter import SecurityHubResourcesTrendsStringFilter


class SecurityHubResourcesTrendsCompositeFilter(BaseModel):
    StringFilters: list[SecurityHubResourcesTrendsStringFilter] | None = None
    NestedCompositeFilters: list[SecurityHubResourcesTrendsCompositeFilter] | None = None
    Operator: Literal['AND', 'OR'] | None = None
