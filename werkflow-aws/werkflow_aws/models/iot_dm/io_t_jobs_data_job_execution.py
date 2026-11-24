from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobsDataJobExecution(BaseModel):
    jobId: StrictStr | None = None
    thingName: StrictStr | None = None
    status: StrictStr | None = None
    statusDetails: dict[StrictStr, StrictStr] | None = None
    queuedAt: StrictInt | None = None
    startedAt: StrictInt | None = None
    lastUpdatedAt: StrictInt | None = None
    approximateSecondsBeforeTimedOut: StrictInt | None = None
    versionNumber: StrictInt | None = None
    executionNumber: StrictInt | None = None
    jobDocument: StrictStr | None = None
