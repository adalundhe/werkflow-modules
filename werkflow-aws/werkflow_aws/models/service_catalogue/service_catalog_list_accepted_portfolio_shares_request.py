from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListAcceptedPortfolioSharesRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
    PortfolioShareType: Literal['IMPORTED', 'AWS_SERVICECATALOG', 'AWS_ORGANIZATIONS'] | None = None
