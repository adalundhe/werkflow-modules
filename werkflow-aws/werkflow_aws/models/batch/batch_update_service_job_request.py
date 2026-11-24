from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchUpdateServiceJobRequest(BaseModel):
    jobId: StrictStr
    schedulingPriority: StrictInt
