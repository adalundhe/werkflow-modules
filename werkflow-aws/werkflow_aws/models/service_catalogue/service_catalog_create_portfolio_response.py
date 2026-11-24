from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_portfolio_detail import ServiceCatalogPortfolioDetail
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogCreatePortfolioResponse(BaseModel):
    PortfolioDetail: ServiceCatalogPortfolioDetail | None = None
    Tags: list[ServiceCatalogTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
