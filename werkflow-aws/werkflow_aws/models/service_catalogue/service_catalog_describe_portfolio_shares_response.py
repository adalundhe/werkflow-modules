from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_portfolio_share_detail import ServiceCatalogPortfolioShareDetail


class ServiceCatalogDescribePortfolioSharesResponse(BaseModel):
    NextPageToken: StrictStr | None = None
    PortfolioShareDetails: list[ServiceCatalogPortfolioShareDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
