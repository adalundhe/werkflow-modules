from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .service_catalog_access_level_filter import ServiceCatalogAccessLevelFilter


class ServiceCatalogSearchProvisionedProductsRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    AccessLevelFilter: ServiceCatalogAccessLevelFilter | None = None
    Filters: dict[Literal['SearchQuery'], list[StrictStr]] | None = None
    SortBy: StrictStr | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
