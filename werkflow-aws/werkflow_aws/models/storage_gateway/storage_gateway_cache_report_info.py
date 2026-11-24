from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_cache_report_filter import StorageGatewayCacheReportFilter
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCacheReportInfo(BaseModel):
    CacheReportARN: StrictStr | None = None
    CacheReportStatus: StrictStr | None = None
    ReportCompletionPercent: StrictInt | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Role: StrictStr | None = None
    FileShareARN: StrictStr | None = None
    LocationARN: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    InclusionFilters: list[StorageGatewayCacheReportFilter] | None = None
    ExclusionFilters: list[StorageGatewayCacheReportFilter] | None = None
    ReportName: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
