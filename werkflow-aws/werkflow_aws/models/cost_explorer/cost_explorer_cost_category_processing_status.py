from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostCategoryProcessingStatus(BaseModel):
    Component: StrictStr | None = None
    Status: StrictStr | None = None
