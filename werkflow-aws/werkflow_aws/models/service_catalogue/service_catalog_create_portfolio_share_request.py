from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .service_catalog_organization_node import ServiceCatalogOrganizationNode


class ServiceCatalogCreatePortfolioShareRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    AccountId: StrictStr | None = None
    OrganizationNode: ServiceCatalogOrganizationNode | None = None
    ShareTagOptions: StrictBool | None = None
    SharePrincipals: StrictBool | None = None
