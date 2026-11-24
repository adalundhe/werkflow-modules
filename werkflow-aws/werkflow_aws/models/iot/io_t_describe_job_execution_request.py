from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDescribeJobExecutionRequest(BaseModel):
    jobId: StrictStr
    thingName: StrictStr
    executionNumber: StrictInt | None = None
