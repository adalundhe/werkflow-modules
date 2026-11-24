from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_record_detail import ServiceCatalogRecordDetail
from .service_catalog_record_output import ServiceCatalogRecordOutput


class ServiceCatalogDescribeRecordResponse(BaseModel):
    RecordDetail: ServiceCatalogRecordDetail | None = None
    RecordOutputs: list[ServiceCatalogRecordOutput] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
