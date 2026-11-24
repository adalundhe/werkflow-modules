from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogCreatePortfolioRequest(BaseModel):
    DisplayName: StrictStr
    ProviderName: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[ServiceCatalogTag] | None = None
