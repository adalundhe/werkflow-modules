from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_portfolio_detail import ServiceCatalogPortfolioDetail


class ServiceCatalogListAcceptedPortfolioSharesResponse(BaseModel):
    PortfolioDetails: list[ServiceCatalogPortfolioDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
