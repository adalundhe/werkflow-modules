from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioned_product_detail import ServiceCatalogProvisionedProductDetail


class ServiceCatalogScanProvisionedProductsResponse(BaseModel):
    ProvisionedProducts: list[ServiceCatalogProvisionedProductDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
