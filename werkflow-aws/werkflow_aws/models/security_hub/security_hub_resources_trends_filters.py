from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_resources_trends_composite_filter import SecurityHubResourcesTrendsCompositeFilter


class SecurityHubResourcesTrendsFilters(BaseModel):
    CompositeFilters: list[SecurityHubResourcesTrendsCompositeFilter] | None = None
    CompositeOperator: Literal['AND', 'OR'] | None = None
