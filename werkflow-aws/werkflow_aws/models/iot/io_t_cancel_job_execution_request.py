from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTCancelJobExecutionRequest(BaseModel):
    jobId: StrictStr
    thingName: StrictStr
    force: StrictBool | None = None
    expectedVersion: StrictInt | None = None
    statusDetails: dict[StrictStr, StrictStr] | None = None
