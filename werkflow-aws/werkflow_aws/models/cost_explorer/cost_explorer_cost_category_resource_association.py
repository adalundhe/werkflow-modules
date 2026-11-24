from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerCostCategoryResourceAssociation(BaseModel):
    ResourceArn: StrictStr | None = None
    CostCategoryName: StrictStr | None = None
    CostCategoryArn: StrictStr | None = None
