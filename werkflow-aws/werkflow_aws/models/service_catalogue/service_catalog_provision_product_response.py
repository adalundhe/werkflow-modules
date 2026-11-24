from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_record_detail import ServiceCatalogRecordDetail


class ServiceCatalogProvisionProductResponse(BaseModel):
    RecordDetail: ServiceCatalogRecordDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
