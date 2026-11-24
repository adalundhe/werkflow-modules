from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogUpdatePortfolioRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    ProviderName: StrictStr | None = None
    AddTags: list[ServiceCatalogTag] | None = None
    RemoveTags: list[StrictStr] | None = None
