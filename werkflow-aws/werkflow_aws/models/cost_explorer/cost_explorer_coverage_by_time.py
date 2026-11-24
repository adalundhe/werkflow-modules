from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_coverage import CostExplorerCoverage
from .cost_explorer_date_interval import CostExplorerDateInterval
from .cost_explorer_reservation_coverage_group import CostExplorerReservationCoverageGroup


class CostExplorerCoverageByTime(BaseModel):
    TimePeriod: CostExplorerDateInterval | None = None
    Groups: list[CostExplorerReservationCoverageGroup] | None = None
    Total: CostExplorerCoverage | None = None
