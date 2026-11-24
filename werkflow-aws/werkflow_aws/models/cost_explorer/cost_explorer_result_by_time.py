from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_group import CostExplorerGroup
from .cost_explorer_metric_value import CostExplorerMetricValue


class CostExplorerResultByTime(BaseModel):
    TimePeriod: CostExplorerDateInterval | None = None
    Total: dict[StrictStr, CostExplorerMetricValue] | None = None
    Groups: list[CostExplorerGroup] | None = None
    Estimated: StrictBool | None = None
