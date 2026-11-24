from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobsDataJobExecutionSummary(BaseModel):
    jobId: StrictStr | None = None
    queuedAt: StrictInt | None = None
    startedAt: StrictInt | None = None
    lastUpdatedAt: StrictInt | None = None
    versionNumber: StrictInt | None = None
    executionNumber: StrictInt | None = None
