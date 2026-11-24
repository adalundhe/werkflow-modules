from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerUpdateCostAllocationTagsStatusError(BaseModel):
    TagKey: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
