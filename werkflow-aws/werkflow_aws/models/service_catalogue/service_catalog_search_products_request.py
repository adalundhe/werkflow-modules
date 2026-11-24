from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogSearchProductsRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    Filters: dict[Literal['FullTextSearch', 'Owner', 'ProductType', 'SourceProductId'], list[StrictStr]] | None = None
    PageSize: StrictInt | None = None
    SortBy: Literal['Title', 'VersionCount', 'CreationDate'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    PageToken: StrictStr | None = None
