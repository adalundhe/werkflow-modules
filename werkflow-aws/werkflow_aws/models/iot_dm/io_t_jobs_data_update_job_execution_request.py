from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTJobsDataUpdateJobExecutionRequest(BaseModel):
    jobId: StrictStr
    thingName: StrictStr
    status: Literal['QUEUED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'REJECTED', 'REMOVED', 'CANCELED']
    statusDetails: dict[StrictStr, StrictStr] | None = None
    stepTimeoutInMinutes: StrictInt | None = None
    expectedVersion: StrictInt | None = None
    includeJobExecutionState: StrictBool | None = None
    includeJobDocument: StrictBool | None = None
    executionNumber: StrictInt | None = None
