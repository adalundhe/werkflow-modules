from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDisassociateProductFromPortfolioRequest(BaseModel):
    ProductId: StrictStr
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
