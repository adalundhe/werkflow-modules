from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTerminateServiceJobsRequest(BaseModel):
    jobs: list[StrictStr]
    reason: StrictStr
