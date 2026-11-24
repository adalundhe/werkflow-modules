from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostCategoryInheritedValueDimension(BaseModel):
    DimensionName: StrictStr | None = None
    DimensionKey: StrictStr | None = None
