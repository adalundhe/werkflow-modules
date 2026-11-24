from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogBudgetDetail(BaseModel):
    BudgetName: StrictStr | None = None
