from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribePendingMaintenanceActionsRequest(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    Filters: list[NeptuneFilter] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
