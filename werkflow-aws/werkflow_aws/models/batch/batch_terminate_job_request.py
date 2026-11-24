from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTerminateJobRequest(BaseModel):
    jobId: StrictStr
    reason: StrictStr
