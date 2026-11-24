from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_findings_trends_composite_filter import SecurityHubFindingsTrendsCompositeFilter


class SecurityHubFindingsTrendsFilters(BaseModel):
    CompositeFilters: list[SecurityHubFindingsTrendsCompositeFilter] | None = None
    CompositeOperator: Literal['AND', 'OR'] | None = None
