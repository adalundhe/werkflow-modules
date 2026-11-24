from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_forecast_result import CostExplorerForecastResult
from .total import Total as CETotal


class CostExplorerGetCostForecastResponse(BaseModel):
    Total: CETotal | None = None
    ForecastResultsByTime: list[CostExplorerForecastResult] | None = None
