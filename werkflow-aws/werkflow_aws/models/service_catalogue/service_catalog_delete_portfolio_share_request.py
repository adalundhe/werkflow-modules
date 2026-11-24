from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_organization_node import ServiceCatalogOrganizationNode


class ServiceCatalogDeletePortfolioShareRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    AccountId: StrictStr | None = None
    OrganizationNode: ServiceCatalogOrganizationNode | None = None
