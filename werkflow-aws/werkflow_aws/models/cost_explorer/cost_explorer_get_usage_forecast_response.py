from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_forecast_result_model import CostExplorerForecastResultModel
from .cost_explorer_metric_value import CostExplorerMetricValue


class CostExplorerGetUsageForecastResponse(BaseModel):
    Total: CostExplorerMetricValue | None = None
    ForecastResultsByTime: list[CostExplorerForecastResultModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
