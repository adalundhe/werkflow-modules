from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTJobsDataDescribeJobExecutionRequest(BaseModel):
    jobId: StrictStr
    thingName: StrictStr
    includeJobDocument: StrictBool | None = None
    executionNumber: StrictInt | None = None
