from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_snapshot_job_error_info import QuickSightSnapshotJobErrorInfo
from .quick_sight_snapshot_job_result import QuickSightSnapshotJobResult


class QuickSightDescribeDashboardSnapshotJobResultResponse(BaseModel):
    Arn: StrictStr | None = None
    JobStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    Result: QuickSightSnapshotJobResult | None = None
    ErrorInfo: QuickSightSnapshotJobErrorInfo | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
