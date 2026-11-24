from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTerminateJobsRequest(BaseModel):
    jobs: list[StrictStr]
    reason: StrictStr
