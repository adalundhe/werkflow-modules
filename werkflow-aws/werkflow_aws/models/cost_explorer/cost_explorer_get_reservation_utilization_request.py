from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_group_definition import CostExplorerGroupDefinition
from .cost_explorer_sort_definition import CostExplorerSortDefinition


class CostExplorerGetReservationUtilizationRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    GroupBy: list[CostExplorerGroupDefinition] | None = None
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY'] | None = None
    Filter: CostExplorerExpression | None = None
    SortBy: CostExplorerSortDefinition | None = None
    NextPageToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
