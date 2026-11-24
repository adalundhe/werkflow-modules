from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudFormationResourceScanSummary(BaseModel):
    ResourceScanId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    PercentageCompleted: StrictFloat | StrictInt | None = None
    ScanType: StrictStr | None = None
