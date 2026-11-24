from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_share_details import ServiceCatalogShareDetails


class ServiceCatalogDescribePortfolioShareStatusResponse(BaseModel):
    PortfolioShareToken: StrictStr | None = None
    PortfolioId: StrictStr | None = None
    OrganizationNodeValue: StrictStr | None = None
    Status: StrictStr | None = None
    ShareDetails: ServiceCatalogShareDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
