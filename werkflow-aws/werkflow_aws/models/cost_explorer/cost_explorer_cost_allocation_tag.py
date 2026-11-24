from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostAllocationTag(BaseModel):
    TagKey: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    LastUpdatedDate: StrictStr | None = None
    LastUsedDate: StrictStr | None = None
