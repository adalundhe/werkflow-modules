from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogSearchProductsAsAdminRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    PortfolioId: StrictStr | None = None
    Filters: dict[Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], list[StrictStr]] | None = None
    SortBy: Literal['Title', 'VersionCount', 'CreationDate'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    PageToken: StrictStr | None = None
    PageSize: StrictInt | None = None
    ProductSource: Literal['ACCOUNT'] | None = None
