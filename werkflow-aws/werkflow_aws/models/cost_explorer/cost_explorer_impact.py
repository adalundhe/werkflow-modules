from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class CostExplorerImpact(BaseModel):
    MaxImpact: StrictFloat | StrictInt | None = None
    TotalImpact: StrictFloat | StrictInt | None = None
    TotalActualSpend: StrictFloat | StrictInt | None = None
    TotalExpectedSpend: StrictFloat | StrictInt | None = None
    TotalImpactPercentage: StrictFloat | StrictInt | None = None
