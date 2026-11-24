from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_budget_detail import ServiceCatalogBudgetDetail


class ServiceCatalogListBudgetsForResourceResponse(BaseModel):
    Budgets: list[ServiceCatalogBudgetDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
