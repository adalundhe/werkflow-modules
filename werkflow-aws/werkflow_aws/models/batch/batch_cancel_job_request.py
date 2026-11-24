from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchCancelJobRequest(BaseModel):
    jobId: StrictStr
    reason: StrictStr
