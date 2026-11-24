from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .service_catalog_product_view_summary import ServiceCatalogProductViewSummary
from .service_catalog_source_connection_detail import ServiceCatalogSourceConnectionDetail


class ServiceCatalogProductViewDetail(BaseModel):
    ProductViewSummary: ServiceCatalogProductViewSummary | None = None
    Status: StrictStr | None = None
    ProductARN: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    SourceConnection: ServiceCatalogSourceConnectionDetail | None = None
