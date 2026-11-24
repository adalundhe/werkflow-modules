from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListPortfoliosForProductRequest(BaseModel):
    ProductId: StrictStr
    AcceptLanguage: StrictStr | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
