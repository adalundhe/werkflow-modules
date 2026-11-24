from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .service_catalog_access_level_filter import ServiceCatalogAccessLevelFilter


class ServiceCatalogScanProvisionedProductsRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    AccessLevelFilter: ServiceCatalogAccessLevelFilter | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
