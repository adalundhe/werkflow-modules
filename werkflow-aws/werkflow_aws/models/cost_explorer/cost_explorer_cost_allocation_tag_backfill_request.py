from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostAllocationTagBackfillRequest(BaseModel):
    BackfillFrom: StrictStr | None = None
    RequestedAt: StrictStr | None = None
    CompletedAt: StrictStr | None = None
    BackfillStatus: StrictStr | None = None
    LastUpdatedAt: StrictStr | None = None
