from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_reservation_aggregates import CostExplorerReservationAggregates
from .cost_explorer_utilization_by_time import CostExplorerUtilizationByTime


class CostExplorerGetReservationUtilizationResponse(BaseModel):
    UtilizationsByTime: list[CostExplorerUtilizationByTime] | None = None
    Total: CostExplorerReservationAggregates | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
