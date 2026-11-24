from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerStartCostAllocationTagBackfillRequest(BaseModel):
    BackfillFrom: StrictStr
