from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_service_action_summary import ServiceCatalogServiceActionSummary


class ServiceCatalogServiceActionDetail(BaseModel):
    ServiceActionSummary: ServiceCatalogServiceActionSummary | None = None
    Definition: dict[StrictStr, StrictStr] | None = None
