from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_comparison_metric_value import CostExplorerComparisonMetricValue
from .cost_explorer_expression import CostExplorerExpression


class CostExplorerCostAndUsageComparison(BaseModel):
    CostAndUsageSelector: CostExplorerExpression | None = None
    Metrics: dict[StrictStr, CostExplorerComparisonMetricValue] | None = None
