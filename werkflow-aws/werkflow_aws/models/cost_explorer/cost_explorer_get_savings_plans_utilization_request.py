from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_sort_definition import CostExplorerSortDefinition


class CostExplorerGetSavingsPlansUtilizationRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY'] | None = None
    Filter: CostExplorerExpression | None = None
    SortBy: CostExplorerSortDefinition | None = None
