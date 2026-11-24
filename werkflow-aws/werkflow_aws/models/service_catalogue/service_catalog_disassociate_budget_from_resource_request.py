from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDisassociateBudgetFromResourceRequest(BaseModel):
    BudgetName: StrictStr
    ResourceId: StrictStr
