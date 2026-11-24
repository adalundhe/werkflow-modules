from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_record_detail import ServiceCatalogRecordDetail


class ServiceCatalogListRecordHistoryResponse(BaseModel):
    RecordDetails: list[ServiceCatalogRecordDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
