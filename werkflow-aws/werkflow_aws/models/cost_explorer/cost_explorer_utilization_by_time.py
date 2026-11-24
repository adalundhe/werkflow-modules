from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_reservation_aggregates import CostExplorerReservationAggregates
from .cost_explorer_reservation_utilization_group import CostExplorerReservationUtilizationGroup


class CostExplorerUtilizationByTime(BaseModel):
    TimePeriod: CostExplorerDateInterval | None = None
    Groups: list[CostExplorerReservationUtilizationGroup] | None = None
    Total: CostExplorerReservationAggregates | None = None
