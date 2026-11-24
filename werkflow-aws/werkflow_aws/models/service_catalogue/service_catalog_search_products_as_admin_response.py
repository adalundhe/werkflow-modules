from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_product_view_detail import ServiceCatalogProductViewDetail


class ServiceCatalogSearchProductsAsAdminResponse(BaseModel):
    ProductViewDetails: list[ServiceCatalogProductViewDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
