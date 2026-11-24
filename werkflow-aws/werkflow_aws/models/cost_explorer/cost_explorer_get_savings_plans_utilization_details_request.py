from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_sort_definition import CostExplorerSortDefinition


class CostExplorerGetSavingsPlansUtilizationDetailsRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    Filter: CostExplorerExpression | None = None
    DataType: list[Literal['ATTRIBUTES', 'UTILIZATION', 'AMORTIZED_COMMITMENT', 'SAVINGS']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortBy: CostExplorerSortDefinition | None = None
