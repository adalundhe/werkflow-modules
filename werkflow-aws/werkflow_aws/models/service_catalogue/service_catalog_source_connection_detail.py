from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_last_sync import ServiceCatalogLastSync
from .service_catalog_source_connection_parameters import ServiceCatalogSourceConnectionParameters


class ServiceCatalogSourceConnectionDetail(BaseModel):
    Type: StrictStr | None = None
    ConnectionParameters: ServiceCatalogSourceConnectionParameters | None = None
    LastSync: ServiceCatalogLastSync | None = None
