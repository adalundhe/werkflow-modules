from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_cache_report_info import StorageGatewayCacheReportInfo


class StorageGatewayListCacheReportsResponse(BaseModel):
    CacheReportList: list[StorageGatewayCacheReportInfo] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
