from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobsDataStartNextPendingJobExecutionRequest(BaseModel):
    thingName: StrictStr
    statusDetails: dict[StrictStr, StrictStr] | None = None
    stepTimeoutInMinutes: StrictInt | None = None
