from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeServerlessV2PlatformVersionsRequest(BaseModel):
    ServerlessV2PlatformVersion: StrictStr | None = None
    Engine: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
    DefaultOnly: StrictBool | None = None
    IncludeAll: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
