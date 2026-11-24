from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_expression import CostExplorerExpression


class CostExplorerGetUsageForecastRequest(BaseModel):
    TimePeriod: CostExplorerDateInterval
    Metric: Literal['BLENDED_COST', 'UNBLENDED_COST', 'AMORTIZED_COST', 'NET_UNBLENDED_COST', 'NET_AMORTIZED_COST', 'USAGE_QUANTITY', 'NORMALIZED_USAGE_AMOUNT', 'LIST_COST', 'CONTRACTED_COST', 'BILLED_COST', 'PUBLIC_EQUIVALENT_BILLED_COST', 'PUBLIC_ON_DEMAND_COST']
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY']
    Filter: CostExplorerExpression | None = None
    BillingViewArn: StrictStr | None = None
    PredictionIntervalLevel: StrictInt | None = None
