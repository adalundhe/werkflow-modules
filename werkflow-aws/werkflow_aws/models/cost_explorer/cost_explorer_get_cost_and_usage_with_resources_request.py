from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression
from .cost_explorer_group_definition import CostExplorerGroupDefinition


class CostExplorerGetCostAndUsageWithResourcesRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY']
    Filter: CostExplorerExpression
    Metrics: list[StrictStr] | None = None
    GroupBy: list[CostExplorerGroupDefinition] | None = None
    BillingViewArn: StrictStr | None = None
    NextPageToken: StrictStr | None = None
