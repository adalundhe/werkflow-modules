from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_comparison_metric_value import CostExplorerComparisonMetricValue
from .cost_explorer_cost_and_usage_comparison import CostExplorerCostAndUsageComparison


class CostExplorerGetCostAndUsageComparisonsResponse(BaseModel):
    CostAndUsageComparisons: list[CostExplorerCostAndUsageComparison] | None = None
    TotalCostAndUsage: dict[StrictStr, CostExplorerComparisonMetricValue] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
