from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTerminateServiceJobRequest(BaseModel):
    jobId: StrictStr
    reason: StrictStr
