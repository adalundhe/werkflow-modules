from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_cache_report_info import StorageGatewayCacheReportInfo


class StorageGatewayDescribeCacheReportResponse(BaseModel):
    CacheReportInfo: StorageGatewayCacheReportInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
