from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_cache_report_filter import StorageGatewayCacheReportFilter
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayStartCacheReportRequest(BaseModel):
    FileShareARN: StrictStr
    Role: StrictStr
    LocationARN: StrictStr
    BucketRegion: StrictStr
    ClientToken: StrictStr
    VPCEndpointDNSName: StrictStr | None = None
    InclusionFilters: list[StorageGatewayCacheReportFilter] | None = None
    ExclusionFilters: list[StorageGatewayCacheReportFilter] | None = None
    Tags: list[StorageGatewayTag] | None = None
