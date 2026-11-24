from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogAssociateBudgetWithResourceRequest(BaseModel):
    BudgetName: StrictStr
    ResourceId: StrictStr
