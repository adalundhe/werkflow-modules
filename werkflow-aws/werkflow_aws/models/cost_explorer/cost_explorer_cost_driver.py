from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_comparison_metric_value import CostExplorerComparisonMetricValue


class CostExplorerCostDriver(BaseModel):
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    Metrics: dict[StrictStr, CostExplorerComparisonMetricValue] | None = None
