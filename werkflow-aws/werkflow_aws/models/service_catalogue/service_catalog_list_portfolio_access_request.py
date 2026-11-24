from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListPortfolioAccessRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    OrganizationParentId: StrictStr | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
