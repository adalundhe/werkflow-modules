from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTDeleteJobExecutionRequest(BaseModel):
    jobId: StrictStr
    thingName: StrictStr
    executionNumber: StrictInt
    force: StrictBool | None = None
    namespaceId: StrictStr | None = None
