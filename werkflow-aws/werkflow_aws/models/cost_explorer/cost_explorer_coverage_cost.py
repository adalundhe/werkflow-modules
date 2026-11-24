from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCoverageCost(BaseModel):
    OnDemandCost: StrictStr | None = None
