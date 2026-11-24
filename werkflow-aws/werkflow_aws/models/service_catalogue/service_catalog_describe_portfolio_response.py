from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_budget_detail import ServiceCatalogBudgetDetail
from .service_catalog_portfolio_detail import ServiceCatalogPortfolioDetail
from .service_catalog_tag import ServiceCatalogTag
from .service_catalog_tag_option_detail import ServiceCatalogTagOptionDetail


class ServiceCatalogDescribePortfolioResponse(BaseModel):
    PortfolioDetail: ServiceCatalogPortfolioDetail | None = None
    Tags: list[ServiceCatalogTag] | None = None
    TagOptions: list[ServiceCatalogTagOptionDetail] | None = None
    Budgets: list[ServiceCatalogBudgetDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
