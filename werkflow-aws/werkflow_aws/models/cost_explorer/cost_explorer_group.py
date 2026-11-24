from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_metric_value import CostExplorerMetricValue


class CostExplorerGroup(BaseModel):
    Keys: list[StrictStr] | None = None
    Metrics: dict[StrictStr, CostExplorerMetricValue] | None = None
