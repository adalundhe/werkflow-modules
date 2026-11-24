from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CostExplorerGetApproximateUsageRecordsRequest(BaseModel):
    Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY']
    ApproximationDimension: Literal['SERVICE', 'RESOURCE']
    Services: list[StrictStr] | None = None
