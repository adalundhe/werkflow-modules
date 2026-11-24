from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListPrincipalsForPortfolioRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
