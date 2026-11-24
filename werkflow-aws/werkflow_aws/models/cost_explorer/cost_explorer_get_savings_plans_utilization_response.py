from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_savings_plans_utilization_aggregates import CostExplorerSavingsPlansUtilizationAggregates
from .cost_explorer_savings_plans_utilization_by_time import CostExplorerSavingsPlansUtilizationByTime


class CostExplorerGetSavingsPlansUtilizationResponse(BaseModel):
    SavingsPlansUtilizationsByTime: list[CostExplorerSavingsPlansUtilizationByTime] | None = None
    Total: CostExplorerSavingsPlansUtilizationAggregates | None = None
    ResponseMetadata: dict[str, Any] | None = None
