from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cloud_formation_scan_filter import CloudFormationScanFilter


class CloudFormationDescribeResourceScanResponse(BaseModel):
    ResourceScanId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    PercentageCompleted: StrictFloat | StrictInt | None = None
    ResourceTypes: list[StrictStr] | None = None
    ResourcesScanned: StrictInt | None = None
    ResourcesRead: StrictInt | None = None
    ScanFilters: list[CloudFormationScanFilter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
