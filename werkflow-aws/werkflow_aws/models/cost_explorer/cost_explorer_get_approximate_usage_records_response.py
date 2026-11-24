from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval


class CostExplorerGetApproximateUsageRecordsResponse(BaseModel):
    Services: dict[StrictStr, StrictInt] | None = None
    TotalRecords: StrictInt | None = None
    LookbackPeriod: CostExplorerDateInterval | None = None
    ResponseMetadata: dict[str, Any] | None = None
