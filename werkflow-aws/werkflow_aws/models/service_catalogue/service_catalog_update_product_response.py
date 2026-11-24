from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_product_view_detail import ServiceCatalogProductViewDetail
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogUpdateProductResponse(BaseModel):
    ProductViewDetail: ServiceCatalogProductViewDetail | None = None
    Tags: list[ServiceCatalogTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
