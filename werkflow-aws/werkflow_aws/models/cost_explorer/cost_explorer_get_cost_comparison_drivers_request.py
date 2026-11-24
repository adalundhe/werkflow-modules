from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_group_definition import CostExplorerGroupDefinition


class CostExplorerGetCostComparisonDriversRequest(BaseModel):
    BaselineTimePeriod: CostExplorerDateInterval
    ComparisonTimePeriod: CostExplorerDateInterval
    MetricForComparison: StrictStr
    BillingViewArn: StrictStr | None = None
    Filter: CostExplorerExpression | None = None
    GroupBy: list[CostExplorerGroupDefinition] | None = None
    MaxResults: StrictInt | None = None
    NextPageToken: StrictStr | None = None
