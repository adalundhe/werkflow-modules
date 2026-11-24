from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_reservation_aggregates import CostExplorerReservationAggregates


class CostExplorerReservationUtilizationGroup(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    Utilization: CostExplorerReservationAggregates | None = None
