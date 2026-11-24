from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogAssociateProductWithPortfolioRequest(BaseModel):
    ProductId: StrictStr
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    SourcePortfolioId: StrictStr | None = None
