from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogRejectPortfolioShareRequest(BaseModel):
    PortfolioId: StrictStr
    AcceptLanguage: StrictStr | None = None
    PortfolioShareType: Literal['IMPORTED', 'AWS_SERVICECATALOG', 'AWS_ORGANIZATIONS'] | None = None
