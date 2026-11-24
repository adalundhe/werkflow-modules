from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_principal import ServiceCatalogPrincipal


class ServiceCatalogListPrincipalsForPortfolioResponse(BaseModel):
    Principals: list[ServiceCatalogPrincipal] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
