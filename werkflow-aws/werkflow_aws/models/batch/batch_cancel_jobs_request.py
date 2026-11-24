from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchCancelJobsRequest(BaseModel):
    jobs: list[StrictStr]
    reason: StrictStr
