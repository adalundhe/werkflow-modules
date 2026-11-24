from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .service_catalog_list_tag_options_filters import ServiceCatalogListTagOptionsFilters


class ServiceCatalogListTagOptionsRequest(BaseModel):
    Filters: ServiceCatalogListTagOptionsFilters | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
