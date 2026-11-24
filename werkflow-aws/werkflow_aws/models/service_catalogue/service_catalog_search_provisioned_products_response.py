from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .service_catalog_provisioned_product_attribute import ServiceCatalogProvisionedProductAttribute


class ServiceCatalogSearchProvisionedProductsResponse(BaseModel):
    ProvisionedProducts: list[ServiceCatalogProvisionedProductAttribute] | None = None
    TotalResultsCount: StrictInt | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
