from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_savings_plans_utilization_aggregates import CostExplorerSavingsPlansUtilizationAggregates
from .cost_explorer_savings_plans_utilization_detail import CostExplorerSavingsPlansUtilizationDetail


class CostExplorerGetSavingsPlansUtilizationDetailsResponse(BaseModel):
    SavingsPlansUtilizationDetails: list[CostExplorerSavingsPlansUtilizationDetail] | None = None
    Total: CostExplorerSavingsPlansUtilizationAggregates | None = None
    TimePeriod: CostExplorerDateInterval | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
