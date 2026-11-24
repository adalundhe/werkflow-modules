from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_sort_definition import CostExplorerSortDefinition


class CostExplorerGetCostCategoriesRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    SearchString: StrictStr | None = None
    CostCategoryName: StrictStr | None = None
    Filter: CostExplorerExpression | None = None
    SortBy: list[CostExplorerSortDefinition] | None = None
    BillingViewArn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextPageToken: StrictStr | None = None
