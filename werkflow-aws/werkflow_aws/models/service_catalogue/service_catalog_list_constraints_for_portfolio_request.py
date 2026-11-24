from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListConstraintsForPortfolioRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    ProductId: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
